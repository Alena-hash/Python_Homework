from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver =  webdriver.Chrome()
driver.get("http://ya.ru/")

url = driver.current_url

print(url)

driver.quit
