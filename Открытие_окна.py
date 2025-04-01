from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link="https://suninjuly.github.io/redirect_accept.html"
    browser=webdriver.Chrome()
    browser.get(link)

    button2=browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button')
    button2.click()

    browser.switch_to.window(browser.window_handles[1])
    new_window = browser.window_handles[1]

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    print(y)

    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(y)

    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

finally:
    time.sleep(10)
    browser.close()