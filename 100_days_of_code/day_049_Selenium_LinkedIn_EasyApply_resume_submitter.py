import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

LINKEDIN_ACCOUNT_EMAIL = os.environ['LINKEDIN_ACCOUNT_EMAIL']
LINKEDIN_ACCOUNT_PASSWORD = os.environ['LINKEDIN_ACCOUNT_PASSWORD']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']

chrome_driver_path = "/Users/angela/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(LINKEDIN_ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(LINKEDIN_ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Locate the apply button
time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(MY_PHONE_NUMBER)

# Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
