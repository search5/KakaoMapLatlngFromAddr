from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time

opts = Options()
opts.headless = True

# This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome(options=opts) as driver:
    wait = WebDriverWait(driver, 10)
    
    driver.get("http://localhost:5000?q=당곡2로 16")

    map_find_result = driver.find_element_by_id("result").text

    map_json = json.loads(map_find_result)
    print(map_json)

    driver.close()
  