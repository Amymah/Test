import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#Open browser
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

#get the page title and print
title: str=driver.title
print("Page title is: ",title)

#Check if the substring is in the title
if "HRM" in title:
    print("Correct title.")
else:
    print("Title is incorrect")

time.sleep(5)

#get heading text (Login page)
Heading =driver.find_element(By.TAG_NAME,"h5").text
print(f"Heading Text:'{Heading}'")  #using f string

time.sleep(5)

#string trimming
Heading_trimmed=Heading.strip()
print(f"Trimmed heading: '{Heading_trimmed}'")

time.sleep(5)

#Convert to upper and lower
print("Uppercase:", Heading_trimmed.upper())
print("Lowercase:", Heading_trimmed.lower())

time.sleep(5)

#String length
print("Length of heading:", len(Heading_trimmed))

time.sleep(5)

# Replace part of string
modified_heading = Heading_trimmed.replace("Login", "Sign In")
print("Replaced Heading:", modified_heading)

time.sleep(5)

#String concatenation
username_text = "Admin"
welcome_msg = "Welcome, " + username_text
print(welcome_msg)

time.sleep(5)

#f-string formatting
print(f"Logging in with username: {username_text}")

time.sleep(5)

#Send keys using strings
driver.find_element(By.NAME, "username").send_keys(username_text)
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.TAG_NAME, "button").click()


time.sleep(3)

#Get Dashboard heading and compare
dashboard_text = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb").text
print("Dashboard Text:", dashboard_text)

time.sleep(5)

if "Dashboard" in dashboard_text:
    print("Login successful and Dashboard loaded")
else:
    print("Dashboard not loaded")

driver.quit()

