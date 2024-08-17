from browser import window, timer, document
import random

GEN_FREQ = 30  # Data generation frequency (Hz)
PLOT_FREQ = 10  # Plot update frequency (Hz)

# Parameters for random walk
noise_level = 0.2  # Noise level added to random walk
data_size = 100  # Number of data points displayed
x_data = list(range(data_size))  # X values (time steps)

# Initialize Y data for two random walks
y_data1 = data_size * [0]  # First random walk data
y_data2 = data_size * [0]  # Second random walk data

# uPlot chart configuration
opts = {
    "title": "Two Random Walks",
    "width": 800,
    "height": 400,
    "scales": {"x": {"time": False}, "y": {"auto": True}},
    "series": [
        {},  # Placeholder for x-axis
        {"label": "Random Walk 1", "stroke": "blue", "width": 2},
        {"label": "Random Walk 2", "stroke": "red", "width": 2},
    ],
}

# Initialize the uPlot chart using Brython
chart = window.uPlot.new(opts, [x_data, y_data1, y_data2], document["chart"])


# Function to generate random walk for the first series
def generate_data1():
    """random walk generator for series 1"""
    global y_data1
    y_data1.pop(0)  # Remove the oldest data point
    prev_y = y_data1[-1]  # Get the last data point
    noise = (random.random() - 0.5) * noise_level  # Add some random noise
    y_data1.append(prev_y + noise)


# Function to generate random walk for the second series
def generate_data2():
    """random walk generator for series 2"""
    global y_data2
    y_data2.pop(0)  # Remove the oldest data point
    prev_y = y_data2[-1]  # Get the last data point
    noise = (random.random() - 0.5) * noise_level  # Add some random noise
    y_data2.append(prev_y + noise)


# Function to plot both series
def plot_data():
    chart.setData([x_data, y_data1, y_data2])


# Set intervals for generating and plotting data
timer.set_interval(generate_data1, 1 / GEN_FREQ * 1000)  # Generate random walk 1
timer.set_interval(generate_data2, 1 / GEN_FREQ * 1000)  # Generate random walk 2
timer.set_interval(plot_data, 1 / PLOT_FREQ * 1000)  # Plot the updated data
