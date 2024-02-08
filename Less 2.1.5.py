from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x_element = x_element.get_attribute('valuex')
    x = x_element
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(20)

finally:
    time.sleep(10)
    browser.quit()
    # 1