import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"


def get_my_latitude_longitude():
    ip = requests.get('https://api.ipify.org').text
    coords = requests.get(f"http://ip-api.com/json/{ip}").json()
    return (coords['lat'], coords['lon'])


MY_LAT, MY_LONG = get_my_latitude_longitude()


def get_iss_coords():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def get_sunrise_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset


def is_iss_over_my_head_now(iss_latitude=None, iss_longitude=None):
    if iss_latitude is None or iss_longitude is None:
        iss_latitude, iss_longitude = get_iss_coords()

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night(sunrise=None, sunset=None):
    time_now = datetime.now().hour
    if sunrise is None or sunset is None:
        sunrise, sunset = get_sunrise_sunset()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    iss_latitude, iss_longitude = get_iss_coords()
    sunrise, sunset = get_sunrise_sunset()

    print("My coords:", MY_LAT, MY_LONG)
    print("ISS Coords:", iss_latitude, iss_longitude)
    print("Sunrise/sunset in my area:", sunrise, sunset)

    if is_iss_over_my_head_now(iss_latitude, iss_longitude) and is_night(sunrise, sunset):
        print("Look Up👆\n\nThe ISS is above you in the sky.")
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
