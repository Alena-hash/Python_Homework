from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(14)
driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

conten = driver.find_element(By.CSS_SELECTOR, "#content")
txt = conten.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)

sleep(5)

