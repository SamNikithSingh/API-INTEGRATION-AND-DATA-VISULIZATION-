# API-INTEGRATION-AND-DATA-VISULIZATION

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : SAM NIKITH SINGH R

*INTERN ID* : CT04DF1181

*DOMAIN NAME* : PYTHON PROGRAMMIMG

*DURATION* : 4 WEEKS

*MENTOR NAME* : NEELA SANTHOSH

*Project Overview*

This project demonstrates how to integrate a public weather API with Python to fetch, process, and visualize real-time weather data for any city. The primary goal of this project is to allow users to choose a city (default is Madurai) and automatically retrieve weather forecast data including temperature, humidity, and precipitation probability using the Open-Meteo API. Once the data is collected, it is analyzed and presented in visual form through various types of graphs and charts.

This serves as a beginner-friendly guide to working with RESTful APIs, data handling using Pandas, and data visualization using Seaborn and Matplotlib. The code is modular and readable, designed for educational, academic, and exploratory data analysis purposes.


-Language
Python 3.x is used as the main programming language due to its simplicity, readability, and powerful ecosystem of data science libraries.
-Libraries & Tools
requests: To make HTTP calls and access the Open-Meteo REST APIs.
pandas: For structured data manipulation and DataFrame operations.
matplotlib: For creating plots and customizing visuals.
seaborn: Built on top of matplotlib, used for easier statistical plotting and enhanced visual appeal.

*APIs Used*

- Open-Meteo Geocoding API
Used to convert a user-friendly place name (like “Madurai”) into latitude and longitude coordinates that can be used in the forecast API.
- Open-Meteo Forecast API
Fetches hourly weather forecast data such as:
Temperature at 2 meters
Relative humidity at 2 meters
Probability of precipitation
Both APIs are public, require no API key, and are ideal for educational or prototype applications.

*How It Works*

City Input & Geocoding:
The script first uses the geocode_location() function to fetch the geographic coordinates of a given city using the Open-Meteo Geocoding API.
Fetch Weather Forecast:
The fetch_forecast() function uses these coordinates to retrieve 7-day hourly weather forecast data in JSON format and converts it into a Pandas DataFrame.
Data Cleaning & Transformation:
The data is processed and timestamps are converted to Python datetime objects for easier plotting and manipulation.
Data Visualization:
The project includes several types of plots:
Line plots for temperature and humidity trends
Histogram showing the distribution of precipitation probability
Heatmap of temperature across hours and dates
These visualizations provide an easy-to-understand weather forecast and showcase how raw API data can be transformed into meaningful insights.

*Functions Overview*

geocode_location(place)
Converts city names to latitude & longitude using Open-Meteo's geocoding service.
fetch_forecast(lat, lon)
Retrieves hourly weather forecasts including temperature, humidity, and precipitation.
These modular functions allow easy customization for other cities or future extensions (e.g., wind speed, pressure).

*Use Cases*

Teaching how to work with public APIs and JSON data in Python.
Demonstrating data visualization techniques for real-world datasets.
Weather analysis tools for researchers, students, or hobbyists.
Foundation for building weather dashboards or mobile weather apps.

*Running the code*

Open the project in Google Colab or Jupyter Notebook.
Install the required libraries if not already available:
python
Copy
Edit
!pip install requests pandas matplotlib seaborn
Run the cells to see the visual output.
You can change "Madurai" to any other city in the function geocode_location("YourCity").

*OUTPUT*


*Future Scope*
Add interactive maps using folium or plotly.
Integrate historical weather data.
Build a GUI using Tkinter or a web dashboard with Streamlit.

*output*
