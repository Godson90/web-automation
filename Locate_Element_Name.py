import time
from selenium import webdriver


driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://localhost/EPsecurity.html")
username= driver.find_elements(by="name", value="Uname") # name of the html element
print("My imput element is : " )
print(username)
time.sleep(15)

driver.quit()
