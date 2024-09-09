from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the Firefox Driver
driver = webdriver.Firefox()

# Accessing the Google page
driver.get("https://www.google.com")

# Find the search box, write the term to be found and submit
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Selenium with Python")
search_box.submit()

# Wait for user input in the terminal before finishing
input()

# Close the browser
driver.quit()