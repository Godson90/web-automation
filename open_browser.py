import time
import selenium
from selenium import webdriver
driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver") # path to the selenium webdrriver executable

driver.get("https://lautech.edu.ng") # opens the browser

time.sleep(60) # keeps the browser open for amount of secs

driver.quit() # closes the browser
