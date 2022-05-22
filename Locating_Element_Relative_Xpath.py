import time
from selenium import webdriver



driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://localhost/EPsecurity.html")
login_form_relative_xpath = driver.find_elements(by="xpath", value="//*[@id="login"] /h1[3]")  #  relative xpath of the html element
print("My login form element ID  is : " )
print(login_form_relative_xpath)
time.sleep(15)

driver.quit()