# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import time

import requests

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
MY_SMTP_ADDRESS = "YOUR EMAIL PROVIDER SMTP SERVER ADDRESS"

BIRTHDAYS_CSV_URL = "https://raw.githubusercontent.com/sidorkinandrew/sidorkinandrew.github.io/mainaster/100-days-of-python/day_032/birthdays.csv"
LETTER_TEMPLATES_URL = "https://raw.githubusercontent.com/sidorkinandrew/sidorkinandrew.github.io/mainaster/100-days-of-python/day_032/letter_{}.txt"

while True:
    today = datetime.now()
    today_tuple = (today.month, today.day)
    print(today_tuple)

    data = pandas.read_csv(BIRTHDAYS_CSV_URL)

    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        file_path = LETTER_TEMPLATES_URL.format(random.randint(1, 3))
        contents = requests.get(file_path).text.strip()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP(MY_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
    else:
        print("Waiting for the date")

    time.sleep(24 * 60 * 60)
