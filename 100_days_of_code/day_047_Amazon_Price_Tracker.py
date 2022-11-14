import requests
import pickle
import os
import lxml
import smtplib
from bs4 import BeautifulSoup

BUY_PRICE = -9999

YOUR_SMTP_ADDRESS = os.environ['YOUR_SMTP_ADDRESS']
YOUR_PASSWORD = os.environ['YOUR_PASSWORD']
YOUR_EMAIL = os.environ['YOUR_EMAIL']


URL = "https://www.amazon.com/Nutri-Pot-Pressure-Non-Stick-Sure-Lock-Technology/dp/B09FNJWJWJ/ref=sr_1_1_sspa?crid=12A5AEB3ZCK7L&keywords=Instant+Pot+Duo+Evo+Plus+10-in-1+Pressure+Cooker%2C&qid=1668465453&sprefix=instant+pot+duo+evo+plus+10-in-1+pressure+cooker%2C%2Caps%2C237&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

if not os.path.exists("page_response.pckl"):
    response = requests.get(URL, headers=HEADERS)
    print("saving response to not disturb Amazon more than needed")
    pickle.dump(response, open("page_response.pckl", "wb"))
else:
    print("loading previously saved response")
    response = pickle.load(open("page_response.pckl", "rb"))

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = float(soup.find(name="span", class_="a-offscreen").getText().replace("$",""))
print(price)

if price < BUY_PRICE:
    message = f"{title} is now at {price}!"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
