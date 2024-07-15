import pandas as pd
import lightningchart as lc

# Load the dataset
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Read the license key
lc.set_license('my_license_key')

# Extract temperature and humidity data
temperature = data['Temperature (C)'].tolist()  # Convert to list
humidity = data['Humidity'].tolist()  # Convert to list

# Create the scatter chart
chart = lc.ScatterChart(
    theme=lc.Themes.White,
    title='Temperature vs Humidity',
    xlabel='Temperature (C)',
    ylabel='Humidity',
    point_shape='circle',
    individual_colors=False
)

# Add data to the scatter chart
series = chart.series.append_samples(
    x_values=temperature,
    y_values=humidity
)

# Set palette colors based on temperature values
series.set_palette_colors(
    steps=[
        {'value': min(temperature), 'color': lc.Color(0, 64, 128)},
        {'value': max(temperature), 'color': lc.Color(255, 128, 64)}
    ],
    look_up_property='x',
    percentage_values=False
)

# Open the chart
chart.open()
