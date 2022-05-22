import time
from selenium import webdriver



driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://localhost/EPsecurity.html")
login_form_full_xpath = driver.find_elements(by="xpath", value="/html/body/div/form") # absolute xpath of the html element
print("My login form element ID  is : " )
print(login_form_full_xpath)
time.sleep(15)

driver.quit()
