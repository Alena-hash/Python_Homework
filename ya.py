from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeServicer
from time import sleep

chrome = webdriver.Chrome()
ff = webdriver.Firefox()
edge = webdriver.Edge()



def make_screenshot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru/")
    sleep(5)
    browser.save_screenshot("./ya_"+browser.name+".png")
    browser.quit()


make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(edge)
