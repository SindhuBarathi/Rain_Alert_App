#!/usr/bin/env python
# coding: utf-8
# This Python code is a script that checks if it's going to rain at a specific geographic location and sends an SMS notification using the Twilio API if rain is expected. Here's a breakdown of the code:

# Import Statements:

# requests: This library is used for making HTTP requests to the OpenWeatherMap (OWM) API to get weather data.
# os: This library provides a way to interact with the operating system and is used to access environment variables.
# twilio.rest.Client: This class from the Twilio library is used to create a client for sending SMS messages.
# Environment Variables:

# API_KEY, account_sid, and auth_token are variables that are expected to contain API keys and authentication credentials. You should replace these empty strings with your actual API keys and Twilio account credentials.
# Geographic Coordinates:

# MY_LAT and MY_LONG are variables representing the latitude and longitude of the location for which you want to check the weather. You can replace these values with the coordinates of your desired location.
# OWM API Request:

# The script constructs a request to the OpenWeatherMap API to get weather data for the specified location. It includes latitude and longitude (lat and lon), the API key (appid), and a parameter to exclude certain weather data ("current," "minutely," and "daily").
# API Request and Data Processing:

# The requests.get() method sends the API request, and the response is processed using JSON. The script checks the weather condition for the first hour (data["hourly"][0]["weather"][0]["id"]) to determine if it's going to rain.
# Rain Prediction:

# The script also checks the next 12 hours of weather data to see if any of the hours indicate rain (if hour["weather"][0]["id"] < 700). If any of these hours have a weather code less than 700, it sets will_rain to True, indicating that it's going to rain.
# Sending SMS:

# If will_rain is True, the script uses the Twilio API to send an SMS message. It creates a Twilio client with the provided account_sid and auth_token, then sends a message to the specified to phone number with the content "It is going to rain, Remember to bring an ☔️".
# Printing Message Status:

# The script prints the status of the sent message, which can be used to verify whether the message was successfully sent.
# Note: To make this script work, you'll need to sign up for an OpenWeatherMap API key and a Twilio account, and replace the empty strings and placeholder values in the code with your actual credentials and desired geographic coordinates.


import requests
import os
from twilio.rest import Client

API_KEY = ""
account_sid = ''
auth_token = ''

MY_LAT = 15.828374
MY_LONG = 80.194435

# MY_LAT = -1.292066
# MY_LONG = 36.821945

# Getting weather data from API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
data_hour1 = data["hourly"][0]["weather"][0]["id"]

data_hour = list(data["hourly"][:12])
will_rain = False
for hour in data_hour:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

# Sending SMS if it rains today
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages         .create(
        body="It is going to rain, Remember to bring an ☔️",
        from_='+14437920004',
        to='+918297736859'
    )
    print(message.status)


# In[ ]:




