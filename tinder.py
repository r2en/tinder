import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        #print("on_exception:Exception occurred!")
        driver.find_element_by_tag_name("body").send_keys(Keys.RIGHT)

def main():
    num = 1
    url = "https://tinder.com/app/login"
    profile = webdriver.FirefoxProfile("/Users/endoutakayoshi/Library/Application Support/Firefox/Profiles/8ng7t5m9.selenium")
    driver = webdriver.Firefox(firefox_profile=profile)
    driver = EventFiringWebDriver(driver, MyListener())

    driver.get(url)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    while num < 10000:
        num = num + 1
        driver.find_element_by_tag_name("body").send_keys(Keys.RIGHT)
        #wait = WebDriverWait(driver, 20)
        wait = WebDriverWait(driver, 100000)
        element = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button.button:nth-child(5)")))
        element.click()
        time.sleep(0.5)
        print(num)
    driver.close()

if __name__ == "__main__":
    main()
