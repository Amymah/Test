import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#Boolean operators: deals with boolean values (True and False)
#Logical operators: works on the boolean values to make logical directions

#Launch the browser
driver = webdriver.Chrome()

#Assignment Operator (=)
url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)

#Arithmetic Operators
username_field_index = 1
password_field_index = 2
total_fields = username_field_index + password_field_index
print(f"Total login field_index expected: {total_fields}")


time.sleep(3)

page_title = driver.title
print(f"Page Title: {page_title}")

#Comparison Operators
if page_title == "OrangeHRM":
    print("Title is correct")
else:
    print("Title is incorrect")

#Membership Operator
if "Orange" in page_title:
    print("'Orange' found in title")
else:
    print("'Orange' not found in title")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

#Assignment with value (Assignment operator)
user_value = "Admin"
pass_value = "admin123"

#Logical Operator
if user_value == "Admin" and pass_value == "admin123":
    print("Credentials are correct")
else:
    print("Credentials are incorrect")

# Use assignment operator
user_value += " (Verified)"
print(user_value)


username.send_keys("Admin")
password.send_keys("admin123")

#Submit form
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(3)

heading = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb").text

# Comparison, Membership, Logical, NOT Operator
if "Dashboard" in heading and not heading == "":
    print("Dashboard loaded successfully")
else:
    print("Dashboard not loaded")

driver.quit()
