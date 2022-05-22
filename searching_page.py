import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver") # path to the selenium webdrriver executable

driver.get("https://python.org") # opens the browser
search= driver.find_element(by="name", value="q").send_keys("pycon" + Keys.ENTER)

time.sleep(10)

driver.quit()