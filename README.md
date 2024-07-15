### Impact of Climate Changes on Extreme Weather Events – Python Analysis

**Introduction**

In today's era of climate change, understanding the correlation between climate shifts and extreme weather events is crucial. This analysis employs Python, a versatile programming language, to explore and visualize data associated with these events.

**How Climate Change Exacerbates Extreme Weather Events**

Climate change intensifies extreme weather events through various mechanisms. Rising global temperatures escalate the intensity and frequency of storms, heatwaves, floods, and droughts. For instance, the increased sea surface temperatures have fueled more powerful hurricanes like Katrina and Harvey, leading to devastating impacts.

**Examples of Extreme Weather Events**

1. **Hurricanes**: Hurricanes are among the most recognizable extreme weather events influenced by climate change. Warmer ocean waters provide more energy, resulting in stronger hurricanes with heavier rainfall and higher wind speeds.

2. **Heatwaves**: Heatwaves are becoming more frequent and severe. The European heatwave of 2019 saw record-breaking temperatures across the continent, impacting agriculture, health, and infrastructure.

**Python**

Python is favored in data analysis for its extensive libraries such as NumPy, Pandas, and visualization tools like LightningChart Python. These resources facilitate efficient data handling, processing, and visualization, making Python indispensable for climate and weather analysis.

**LightningChart Python**

***Overview of LightningChart Python***

LightningChart Python is a powerful library designed for high-performance data visualization. It offers a range of advanced chart types and customization options suitable for analyzing complex weather data.

**Features and Chart Types to Be Used in the Project**

In this project, we will utilize various chart types available in LightningChart to visualize sea level data:
- **Bar Chart**
- **3D Box Chart**
- **Box Plot**
- **Scotter Chart**
- **Pie  Chart**

**Performance Characteristics**
LightningChart is known for its exceptional performance, handling large datasets with ease and providing smooth interactions and animations.

**Setting Up Python Environment**

***Installing Python and Necessary Libraries**

To get started, you need to have Python installed on your system. You can download Python from the official website. Additionally, you will need to install the following libraries:
```
pip install    pandas    lightningchart
```
***Overview of Libraries Used***
- ***Pandas:*** For data manipulation and analysis.
- ***LightningChart:*** For creating high-performance visualizations.

***Setting Up Your Development Environment***
Set up your development environment by installing the required libraries and organizing your project files, including the sea level data files.

**Loading and Processing Data**

***How to Load the Data Files***
You can load the sea level data files using Pandas. Here’s an example:
```
data = pd.read_csv(‘weatherHistory.csv’)
data = pd.read_csv(‘ContiguousU.S.ExtremesInMaximumTemperature.csv’)
```

**Bar Chart:**

The Bar Chart visualizes 'Much Above Normal' and 'Much Below Normal' temperature extremes across the United States from 1910 to 2021.

```python
import pandas as pd
import lightningchart as lc

# Set license key
lc.set_license('my_license_key')

# Load data
data = pd.read_csv('ContiguousU.S.ExtremesInMaximumTemperature.csv')

# Prepare data for the combined Bar Chart
categories = data['Date'].astype(str).tolist()
data_combined = [
    {'subCategory': 'Much Above Normal', 'values': data['Much Above Normal'].tolist()},
    {'subCategory': 'Much Below Normal', 'values': data['Much Below Normal'].tolist()}
]

# Create the combined Bar Chart
bar_chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.White,
    title='Contiguous U.S. Extremes in Maximum Temperature'
)

# Set data for the combined Bar Chart
bar_chart.set_data_grouped(categories, data_combined)
bar_chart.set_bars_margin(0.1)
bar_chart.open(method='browser')
```
![bar chart](/images/bar.png)

This chart provides a historical perspective on temperature anomalies in the United States, highlighting periods of extreme weather conditions.

**3D Box Chart: **

The 3D Chart displays average temperature, apparent temperature, humidity, and wind speed by weather type.

```python
import pandas as pd
from lightningchart import Themes, Chart3D

# Set license key
my_license_key = 'my_license_key'

# Load data
data = pd.read_csv('weatherHistory.csv')

# Calculate averages by weather type
avg_weather_data = data.groupby('Summary')[['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)']].mean().reset_index()

# Prepare data for 3D chart
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

# Add box series for temperature, apparent temperature, humidity, and wind speed
box_series_temp = chart_3d.add_box_series()
box_series_temp.set_name('Temperature')

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

box_series_temp.add(data_boxes_temp)

box_series_temp_app = chart_3d.add_box_series()
box_series_temp_app.set_name('Apparent Temperature')

data_boxes_app_temp = [
    {
        'xCenter': i * 4 + 1,
        'yCenter': apparent_temp_values[i] / 2,
        'zCenter': 1,
        'xSize': 4,
        'ySize': apparent_temp_values[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

box_series_temp_app.add(data_boxes_app_temp)

box_series_humidity = chart_3d.add_box_series()
box_series_humidity.set_name('Humidity')

data_boxes_humidity = [
    {
        'xCenter': i * 4 + 2,
        'yCenter': humidities[i] / 2,
        'zCenter': 2,
        'xSize': 4,
        'ySize': humidities[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

box_series_humidity.add(data_boxes_humidity)

box_series_wind_speed = chart_3d.add_box_series()
box_series_wind_speed.set_name('Wind Speed')

data_boxes_wind_speed = [
    {
        'xCenter': i * 4 + 3,
        'yCenter': wind_speeds[i] / 2,
        'zCenter': 3,
        'xSize': 4,
        'ySize': wind_speeds[i],
        'zSize': 0.2
    }
    for i in range(len(categories))
]

box_series_wind_speed.add(data_boxes_wind_speed)

chart_3d.open(method='browser')
```
![3d chart](/images/3d.png)

This chart offers a comprehensive view of weather variables across different weather types, enabling analysts to observe patterns and correlations between temperature, humidity, and wind speed.

**Box Plot:**

The Box Plot illustrates temperature distributions by weather summary, offering insights into temperature variability across different weather conditions.

```python
import pandas as pd
import lightningchart as lc
import numpy as np

# Set license key
lc.set_license('my_license_key')

# Load data
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Convert 'Formatted Date' to datetime
data['Formatted Date'] = pd.to_datetime(data['Formatted Date'], utc=True)

# Group data by weather summary and temperature
grouped_data = data.groupby('Summary')['Temperature (C)'].apply(list)

# Convert grouped data to list of lists for box plot
box_plot_data = grouped_data.tolist()

# Create XY chart
chart = lc.ChartXY(
    title='Temperature Distribution by Weather Summary',
    theme=lc.Themes.White
)

# Function to add box plot to chart
def add_box_plot_to_chart(chart, column_data, column_name, column_index):
    q1 = np.percentile(column_data, 25)
    q3 = np.percentile(column_data, 75)
    median = np.median(column_data)
    min_val = np.min(column_data)
    max_val = np.max(column_data)
    
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

# Add each weather summary as a separate box plot
for i, (label, values) in enumerate(zip(grouped_data.index, box_plot_data)):
    add_box_plot_to_chart(chart, values, label, i)

# Customize x-axis labels
x_axis = chart.get_default_x_axis()
x_axis.set_title('Weather Summary')
x_axis.set_scroll_strategy('fitting')

# Customize y-axis title
y_axis = chart.get_default_y_axis()
y_axis.set_title('Temperature (C)')

chart.open(method='browser')
```
![box plot](/images/box.png)
This chart provides a clear view of temperature distributions across different weather summaries, highlighting variability and central tendencies within each category.

**Scatter Chart:**

The Scatter Plot depicts the relationship between temperature and humidity, utilizing color to indicate temperature variations.

```python
import pandas as pd
import lightningchart as lc

# Load data
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Set license key
lc.set_license('my_license_key')

# Extract temperature and humidity data
temperature = data['Temperature (C)'].tolist()
humidity = data['Humidity'].tolist()

# Create Scatter Chart
chart = lc.ScatterChart(
    theme=lc.Themes.White,
    title='Temperature vs Humidity',
    xlabel='Temperature (C)',
    ylabel='Humidity',
    point_shape='circle',
    individual_colors=False
)

# Add data to Scatter Chart
series = chart.series.append_samples(
    x_values=temperature,
    y_values=humidity
)

# Set palette colors based on temperature values
series.set_palette_colors(
    steps=[
        {'value':

 -10, 'color': '#0000FF'},
        {'value': 0, 'color': '#00FFFF'},
        {'value': 10, 'color': '#00FF00'},
        {'value': 20, 'color': '#FFFF00'},
        {'value': 30, 'color': '#FF0000'}
    ]
)

chart.open(method='browser')
```
![scotter](/images/scatter.png)

This Scatter Plot effectively visualizes the relationship between temperature and humidity, highlighting how temperature changes influence humidity levels across different weather conditions.

**Pie Chart:**

The Pie Chart displays the distribution of weather types in categorical form.

```python
import pandas as pd
import lightningchart as lc

# Set license key
lc.set_license('my_license_key')

# Load data
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Group data by weather summary
grouped_data = data['Summary'].value_counts()

# Create Pie Chart
chart = lc.PieChart(
    theme=lc.Themes.Dark,
    title='Distribution of Weather Types'
)

# Add data to Pie Chart
for category, value in grouped_data.items():
    chart.add_slice(value, category)

chart.open(method='browser')
```
![pie](/images/pie.png)
The Pie Chart offers a straightforward representation of weather type distributions, providing a quick overview of prevailing weather conditions over the dataset period.

---

This article integrates Python's capabilities with LightningChart Python to analyze and visualize climate and weather data effectively. Each chart example is accompanied by Python code and a brief analysis, demonstrating practical applications in climate research and analysis.

**Conclusion**

***Recap of Creating the Application and Its Usefulness***

In this project, we explored the impact of climate change on extreme weather events using Python for data analysis and visualization. We utilized various powerful tools and libraries, including LightningChart Python, to create insightful visual representations of weather data. Each chart served a specific purpose, from analyzing temperature distributions to understanding the relationship between humidity and temperature variations.

Python's versatility allowed us to handle large datasets efficiently, preprocess data for analysis, and visualize complex relationships with ease. The combination of Python's data analysis capabilities and LightningChart Python's visualization tools provided a robust platform for exploring and interpreting climate and weather data.

***Benefits of Using LightningChart Python for Visualizing Data***

- LightningChart Python offers exceptional performance, capable of handling large datasets and rendering complex visualizations swiftly. This is crucial for real-time analysis and interactive exploration of weather patterns.

- The library provides a wide range of chart types, from traditional bar charts and scatter plots to advanced 3D visualizations and interactive pie charts. This versatility allows researchers and analysts to choose the most suitable visualization method for their data.

- LightningChart Python allows extensive customization of charts, including themes, colors, annotations, and interactive features. This flexibility enables users to tailor visualizations to specific requirements and enhance the clarity of insights.

- Being integrated seamlessly with Python, LightningChart Python can leverage the vast ecosystem of Python libraries for data handling, preprocessing, and analysis. This integration simplifies workflows and enhances productivity.

- Despite its powerful features, LightningChart Python remains user-friendly, with intuitive APIs and comprehensive documentation. This accessibility makes it suitable for both novice users and experienced data scientists.

In conclusion, the combination of Python and LightningChart Python offers a compelling solution for analyzing and visualizing climate and weather data. Whether exploring long-term climate trends, studying the impact of extreme weather events, or communicating findings effectively, these tools empower researchers to gain deeper insights into the complex dynamics of our changing climate.

---

**Sources:**
- Climate.gov US Climate Extremes Index: [Link](https://www.climate.gov/maps-data/dataset/us-climate-extremes-index-graph-or-map)
- NOAA Climate Extremes Index: [Link](https://www.ncei.noaa.gov/access/monitoring/cei/graph/us/1/01-12)
- Python Official Website: [Link](https://www.python.org/)
- LightningChart Python Documentation: [Link](https://lightningchart.com/python-charts/docs/charts/)
- Our World in Data - US Weather & Climate: [Link](https://ourworldindata.org/us-weather-climate)


