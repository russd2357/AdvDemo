import requests
import pandas as pd
import streamlit as st

# Title of the Streamlit app
st.title("Weather Data Table")

# Define the endpoint for the Open-Meteo API
latitude = 52.52  # Example latitude for Berlin
longitude = 13.41  # Example longitude for Berlin
url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'

# Make a GET request to the Open-Meteo API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    
    # Convert the JSON data to a pandas DataFrame
    df = pd.DataFrame(weather_data['hourly']['temperature_2m'], columns=['Temperature'])
    df['Time'] = pd.to_datetime(weather_data['hourly']['time'])
    
    # Display the DataFrame using Streamlit
    st.write(df)
else:
    st.error(f"Error: {response.status_code}")