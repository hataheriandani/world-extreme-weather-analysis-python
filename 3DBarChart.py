import pandas as pd
from lightningchart import Themes, Chart3D

# Place your license key here
my_license_key = 'my_license_key'

# Load the data
data = pd.read_csv('weatherHistory.csv')

# Calculate average temperature, humidity, and wind speed by weather type
avg_weather_data = data.groupby('Summary')[['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)']].mean().reset_index()

# Extract data for plotting
categories = avg_weather_data['Summary'].tolist()
temperatures = avg_weather_data['Temperature (C)'].tolist()
apparent_temp_values = avg_weather_data['Apparent Temperature (C)'].tolist()
humidities = avg_weather_data['Humidity'].tolist()
wind_speeds = avg_weather_data['Wind Speed (km/h)'].tolist()

# Create 3D chart
chart_3d = Chart3D(
    theme=Themes.White,
    title='Average Temperature, Apparent Temperature, Humidity, and Wind Speed by Weather Type',
    license=my_license_key
)

# Add box series for temperature
box_series_temp = chart_3d.add_box_series()
box_series_temp.set_name('Temperature')

# Prepare data for the temperature box chart
data_boxes_temp = [
    {
        'xCenter': i * 4 + 1,
        'yCenter': temperatures[i] / 2,
        'zCenter': 0,
        'xSize': 4,
        'ySize': temperatures[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

# Add data for temperature boxes
box_series_temp.add(data_boxes_temp)

# Add box series for apparent temperature
box_series_temp_app = chart_3d.add_box_series()
box_series_temp_app.set_name('Apparent Temperature')

# Prepare data for the Apparent Temperature box chart
data_boxes_app_temp = [
    {
        'xCenter': i * 4 + 1,
        'yCenter': apparent_temp_values[i] / 2,
        'zCenter': 1,  # Set a distance of 1 unit along the z-axis
        'xSize': 4,
        'ySize': apparent_temp_values[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

# Add data for apparent temperature boxes
box_series_temp_app.add(data_boxes_app_temp)

# Add box series for humidity
box_series_humidity = chart_3d.add_box_series()
box_series_humidity.set_name('Humidity')

# Prepare data for the humidity box chart
data_boxes_humidity = [
    {
        'xCenter': i * 4 + 2,  # Place humidity boxes 2 units away along the x-axis
        'yCenter': humidities[i] / 2,
        'zCenter': 2,
        'xSize': 4,
        'ySize': humidities[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

# Add data for humidity boxes
box_series_humidity.add(data_boxes_humidity)

# Add box series for wind speed
box_series_wind_speed = chart_3d.add_box_series()
box_series_wind_speed.set_name('Wind Speed')

# Prepare data for the wind speed box chart
data_boxes_wind_speed = [
    {
        'xCenter': i * 4 + 3,  # Place wind speed boxes 3 units away along the x-axis
        'yCenter': wind_speeds[i] / 2,
        'zCenter': 3,
        'xSize': 4,
        'ySize': wind_speeds[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

# Add data for wind speed boxes
box_series_wind_speed.add(data_boxes_wind_speed)

# Add legend
chart_3d.add_legend(title='Weather Variables' , x= 15 ,y=35, data=chart_3d)

# Open the chart in browser
chart_3d.open(method='browser')
