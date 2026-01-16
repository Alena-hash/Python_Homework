from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver =  webdriver.Chrome()
driver.get("https://ya.ru/")

current_title = driver.title

print(current_title)

driver.quit()

