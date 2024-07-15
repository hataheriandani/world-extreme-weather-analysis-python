
import pandas as pd
import lightningchart as lc
import numpy as np

# Read the license key from a file
lc.set_license('my_license_key')

# Load the dataset
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Convert 'Formatted Date' to datetime
data['Formatted Date'] = pd.to_datetime(data['Formatted Date'], utc=True)

# Extract necessary data for the box plot (Temperature by Summary)
grouped_data = data.groupby('Summary')['Temperature (C)'].apply(list)

# Convert grouped data to list of lists for the box plot
box_plot_data = grouped_data.tolist()

# Create a single chart
chart = lc.ChartXY(
    title='Temperature Distribution by Weather Summary',
    theme=lc.Themes.White
)

# Function to add a box plot to the chart
def add_box_plot_to_chart(chart, column_data, column_name, column_index):
    # Calculate box plot statistics
    q1 = np.percentile(column_data, 25)
    q3 = np.percentile(column_data, 75)
    median = np.median(column_data)
    min_val = np.min(column_data)
    max_val = np.max(column_data)
    
    # Add box plot series
    series = chart.add_box_series()
    series.add(
        start=column_index - 0.4,
        end=column_index + 0.4,
        median=float(median),
        lower_quartile=float(q1),
        upper_quartile=float(q3),
        lower_extreme=float(min_val),
        upper_extreme=float(max_val)
    )
    series.set_name(column_name)

# Add each weather summary as a separate box plot to the same chart
for i, (label, values) in enumerate(zip(grouped_data.index, box_plot_data)):
    add_box_plot_to_chart(chart, values, label, i)

# Customize x-axis labels
x_axis = chart.get_default_x_axis()
x_axis.set_title('Weather Summary')
x_axis.set_scroll_strategy('fitting')
x_axis.set_tick_strategy('Empty')

# Add custom ticks with labels
for i, label in enumerate(grouped_data.index):
    custom_tick = x_axis.add_custom_tick('major')
    custom_tick.set_value(i)
    custom_tick.set_text(label)
    custom_tick.set_tick_label_rotation(270)

# Customize y-axis title
y_axis = chart.get_default_y_axis()
y_axis.set_title('Temperature (C)')

# Open the chart
chart.open(method='browser')  # Use 'notebook' if you are working in a Jupyter notebook