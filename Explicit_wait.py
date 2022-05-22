import BY as BY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://python.org")

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(BY.ID))

finally:
    driver.quit()
