import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://localhost/formfilling.html")
select= Select(driver.find_element(by="id", value= "numReturnSelect"))
select.select_by_value("250") # selecting value from drop down list
time.sleep(3)
select.select_by_visible_text("200") # selecting text from drop down list
time.sleep(3)
submit_drop_down = driver.find_element(by="name", value= "continue") # clicks the submit button by the drop down list
submit_drop_down.submit()
time.sleep(3)
driver.quit()

driver.quit()
