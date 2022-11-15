from selenium import webdriver
import time

from selenium.webdriver.common.by import By
TIME_CHECKS = 3

path_to_driver = "/temp/chromedriver.exe"
url = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome(executable_path=path_to_driver)
driver.get(url=url)

time.sleep(5)

language_select = driver.find_element(By.CSS_SELECTOR, "#promptContentChangeLanguage #langSelect-EN")
language_select.click()

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")
start_time = time.time()
increment = TIME_CHECKS

while True:
    if time.time() > increment + start_time:
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
            for item in upgrades[::-1]:
                print("Buying "+ item.text)
                item.click()
                item.click()
        except:
            print("No upgrades available")

        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")
            for item in products[::-1]:
                print("Buying "+ item.text)
                item.click()
                item.click()
        except:
            print("Not enough cookies")

        start_time = time.time()
        increment += TIME_CHECKS
    cookie.click()
