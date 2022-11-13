# Monday Motivation Project
import smtplib
import datetime as dt
import requests
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"
QUOTES_URL = "https://raw.githubusercontent.com/sidorkinandrew/sidorkinandrew.github.io/mainaster/100-days-of-python/day_032/quotes.txt"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:

    all_quotes = requests.get(QUOTES_URL).text.strip().split("\n")
    quote = random.choice(all_quotes)

    print(quote)
    print('the quote above will be sent')

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation Quote\n\n{quote}"
        )
