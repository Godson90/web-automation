from selenium import webdriver

driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.implicitly_wait(10)
driver.get("http://python.org")
dynamic_element= driver.find_element(by="id", value= "start-shell")

driver.quit()