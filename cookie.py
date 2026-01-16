from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get("https://labirint.ru/")
driver.add_cookie(my_cookie)

cookies = driver.get_cookies()
print(cookies)
# driver.refresh()
# driver.delete_all_cookies()

# sleep(10)

driver.quit
