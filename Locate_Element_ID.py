import time
from selenium import webdriver


driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://localhost/EPsecurity.html")
login_form_id = driver.find_elements(by="id", value="login") # ID of the html element
print("My login form element ID  is : " )
print(login_form_id)
time.sleep(15)

driver.quit()
