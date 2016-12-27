from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from writeToDisk import *

driverLocation = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(driverLocation)
driver.get("http://www.python.org")
print(driver.title)

assert "Python" in driver.title

# Go to the search text field
elem = driver.find_element_by_name("q")
 # If this element is a text entry element, this will clear the value.
elem.clear()
# Type pycon in the search text field
elem.send_keys("pycon")
# Essentially click the go button
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.get("http://www.python.org")
elem2 = driver.find_element_by_link_text("Start with our Beginner’s Guide")
# Opens the new beginner's guide page
elem2.click()

# Close the page
driver.close()