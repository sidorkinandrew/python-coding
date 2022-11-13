import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "8f14ac1ce7426fef035aa2a985c43017"
account_sid = "******************"
auth_token = "******************"

def get_my_latitude_longitude():
    ip = requests.get('https://api.ipify.org').text
    coords = requests.get(f"http://ip-api.com/json/{ip}").json()
    return (coords['lat'], coords['lon'])

my_latitude, my_longitude = get_my_latitude_longitude()

weather_params = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_= os.environ['TWILIO_NUMBER'],
        to=os.environ['MY_NUMBER']
    )
    print(message.status)
