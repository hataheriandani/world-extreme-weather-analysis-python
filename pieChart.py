import pandas as pd
import lightningchart as lc

# Load the dataset
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Read the license key from a file
lc.set_license('my_license_key')

# Assuming the correct column name is 'Summary' (based on the printed columns)
weather_counts = data['Summary'].value_counts().reset_index()
weather_counts.columns = ['Summary', 'Count']

# Prepare the data for the pie chart
pie_data = [{'name': row['Summary'], 'value': row['Count']} for index, row in weather_counts.iterrows()]

# Create the pie chart
chart = lc.PieChart(
    labels_inside_slices=False,
    title='Weather Distribution Pie Chart',
    theme=lc.Themes.White
)
chart.add_slices(pie_data)
chart.set_inner_radius(50)
chart.open()
