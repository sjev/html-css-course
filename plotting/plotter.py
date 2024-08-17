from browser import window, timer, document
import math
import random

GEN_FREQ = 50
PLOT_FREQ = 50


# Basic sine wave parameters
amplitude = 1  # Amplitude of the sine wave
frequency = 0.1  # Frequency for sine calculation
noise_level = 0.2  # Noise level added to sine wave
data_size = 100  # Number of data points displayed
x_data = list(range(data_size))  # X values (time steps)
y_data = data_size * [0]  # Initial sine wave Y values

# uPlot chart configuration
opts = {
    "title": "Sine Wave with Noise (5 Hz plotting)",
    "width": 800,
    "height": 400,
    "scales": {"x": {"time": False}, "y": {"auto": True}},
    "series": [
        {},  # Placeholder for x-axis
        {"label": "Sine + Noise", "stroke": "blue", "width": 2},
    ],
}

# Initialize the uPlot chart using Brython
chart = window.uPlot.new(opts, [x_data, y_data], document["chart"])


# Function to generate sine wave with superimposed noise (10 Hz)
def generate_data():
    """random walk generator"""
    global y_data
    y_data.pop(0)  # Remove the oldest data point

    prev_y = y_data[-1]  # Get the last data point

    noise = (random.random() - 0.5) * noise_level  # Add some random noise

    y_data.append(prev_y + noise)


# Function to plot data (5 Hz)
def plot_data():
    chart.setData([x_data, y_data])


# Set intervals for both generating and plotting data
timer.set_interval(
    generate_data, 1 / GEN_FREQ * 1000
)  # Generate sine wave with noise at 10 Hz
timer.set_interval(plot_data, 1 / PLOT_FREQ * 1000)  # Plot the updated data at 5 Hz
