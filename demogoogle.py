from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("http://www.google.com/search?q=csun")
atags=driver.find_elements_by_tag_name("a")
for tag in atags:
    # tag.find_element_by_xpath("./..")
    tag.parent