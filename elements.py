from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ya.ru/")

element = driver.find_element(By.CSS_SELECTOR, "#text")
element.clear()
element.send_keys("test skypro")

element.click()

driver.find_element(By.CSS_SELECTOR, "button[typesubmit]").click()
sleep(10)


print(element)

driver.quit
