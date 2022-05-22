import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\Selenium_Chrome_WebDriver\chromedriver")
driver.get("http://jqueryui.com/droppable")
driver.switch_to.frame(0)  # the frame of the drag and drop
action_chains= ActionChains(driver)

source_drag= driver.find_element(by="id", value="draggable") # id of drag
destination_drop= driver.find_element(by="id", value="droppable") # id of drop

action_chains.drag_and_drop_by_offset(source_drag, 50, 50).perform()
time.sleep(3)
action_chains.drag_and_drop(source_drag, destination_drop).perform()
time.sleep(4)
driver.quit()