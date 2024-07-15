import pandas as pd
import lightningchart as lc

# Place your license key here
lc.set_license('my_license_key')

# Read the data from a CSV file
data = pd.read_csv('ContiguousU.S.ExtremesInMaximumTemperature.csv')

# Prepare data for the combined Bar Chart
categories = data['Date'].astype(str).tolist()
data_combined = [
    {'subCategory': 'Much Above Normal', 'values': data['Much Above Normal'].tolist()},
    {'subCategory': 'Much Below Normal', 'values': data['Much Below Normal'].tolist()}
]

# Create the combined Bar Chart
bar_chart = lc.BarChart(
    vertical=True,  # Vertical orientation of bars
    theme=lc.Themes.White,
    title='Contiguous U.S. Extremes in Maximum Temperature'
)

# Disable sorting (optional)
bar_chart.set_sorting('disabled')

# Set data for the combined Bar Chart
bar_chart.set_data_grouped(categories, data_combined)

# Set the margin around each bar along category axis as percentage of bar thickness
bar_chart.set_bars_margin(0.1)  # Set margin to 10%
# add legend
bar_chart.add_legend(title='Legend',x=15,y=80, data=bar_chart)

# Open the combined Bar Chart
bar_chart.open(method='browser')
