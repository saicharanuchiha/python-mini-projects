import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
to_number = os.environ.get("MY_PHONE_NUMBER")
from_number = os.environ.get("TWILIO_PHONE_NUMBER")
MY_LAT = 20.466999
MY_LONG = 85.077888

parameters = {
    "lat": MY_LAT,
    "lon":MY_LONG,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to= to_number,
        from_=from_number,
        body="It's going to rain today. Remember to bring an ☂️",
    )

    print(message.status)