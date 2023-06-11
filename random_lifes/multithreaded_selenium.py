from concurrent.futures.thread import ThreadPoolExecutor

import numpy as np
import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import random
import pandas as pd
import time
from datetime import datetime as dt
import pickle
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver_path = "C:\\temp\\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

language_code = "en"

def driver_setup():
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--headless')
    options.add_argument(f'--lang={language_code}')

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def create_cache(domains):
    return dict(zip([i['Url'] for i in domains], [i['Url'] for i in domains]))

file_path = 'domains.pckl'
tc_domains = pickle.load(open(file_path, 'rb'))
print(f"Loaded {len(tdomains)} domains")

URLS = [i['Url'] for i in domains]
print(f"Loaded {len(URLS)} domains")

domain_cache = create_cache(tc_domains)

scan_results = {}

def merge_str(astring):
    return astring.replace('\n', '')

def fetcher(url, driver):
    print(f"{URLS.index(url)+1} / {len(URLS)}: {str(dt.utcnow())}", "processing ... ", url, {domain_cache.get(url)})
    error, text = False, ''
    try:
        driver.get("https://"+url)
    except Exception as e:
        print(f'{url} website not found', merge_str(e.__dict__['msg']))
        error = 'website not found'
        #scan_results[url]['error'] = 'website not found'
        #scan_results[url]['text'] = e.__dict__['msg']
        text = merge_str(e.__dict__['msg'])
        return error, text # continue
    print(f'{url} sleeping 5 secs')
    time.sleep(5)
    try:
        iframe = driver.find_element(By.ID, 'iframe_id')
    except Exception as e:
        print(f'{url} no iframe detected')
        #scan_results[url]['error'] = 'no iframe detected'
        error = 'no iframe detected'
        driver.switch_to.default_content()
        el = driver.find_element(By.XPATH, 'html/body')
        print(f'{url} el.text[0:64]', merge_str(el.text[0:64]))
        #scan_results[url]['text'] = el.text[0:len("Error 404")]
        text = merge_str(el.text[0:64])
        return error, text # continue
    driver.switch_to.frame(iframe)
    iframe_navbar = driver.find_element(By.CLASS_NAME, 'nav-bar-1')
    print(f'{url} iframe_navbar.text', merge_str(iframe_navbar.text[:64]))
    error, text = False, iframe_navbar.text
    return error, merge_str(text)

def crawler(lst, driver):
    print(f"Crawler {drivers.index((driver))} is running")
    for i, url in enumerate(lst):
        scan_results[url] = {}
        #print(f"{i+1} / {len(URLS)}: {str(dt.utcnow())}", "processing ... ", url)
        scan_results[url]['error'], scan_results[url]['text'] = fetcher(url, driver)
    return scan_results


MAX_THREADS = 6

drivers = [driver_setup() for _ in range(MAX_THREADS)]
chunks = np.array_split(URLS, MAX_THREADS)
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    bucket = executor.map(crawler, chunks, drivers)

pickle.dump(scan_results, open('scan_results.cpkl', 'wb'))

for i in scan_results:
    print(i,end=" ")
    try:
        print(str(scan_results[i]['text']).replace('\n', ' '),end=" ")
        print(scan_results[i]['error'])
    except Exception as e:
        pass

[driver.quit() for driver in drivers]

print('YAY!!!!')
