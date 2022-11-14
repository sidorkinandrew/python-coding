import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\temp\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

# PART 1 - Locate a price on the amazon.com page of the selected good

URL = "https://www.amazon.com/Nutri-Pot-Pressure-Non-Stick-Sure-Lock-Technology/dp/B09FNJWJWJ/ref=sr_1_1_sspa?crid=12A5AEB3ZCK7L&keywords=Instant+Pot+Duo+Evo+Plus+10-in-1+Pressure+Cooker%2C&qid=1668465453&sprefix=instant+pot+duo+evo+plus+10-in-1+pressure+cooker%2C%2Caps%2C237&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

driver.get(URL)
# price = driver.find_element(By.CSS_SELECTOR, "span.a-price.aok-align-center")
price = driver.find_element(By.CSS_SELECTOR, "div#corePrice_feature_div.celwidget")
# price = driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[1]')

print(dir(price))
print(price.text.strip())

print(type(price.text))

driver.close()

## PART 2 - parse python.org for upcoming events

URL = "https://www.python.org/"
driver.get(URL)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
#
# for atime in event_times:
#     print(atime.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

pprint(events)

driver.quit()
