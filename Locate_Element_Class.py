import time
from selenium import webdriver


driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")

driver.get("http://localhost/EPsecurity.html")
content= driver.find_elements(by="class_name", value="login") # class of the html element
print("My class element is : " )
print(content)
time.sleep(15)

driver.quit()
