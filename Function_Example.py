import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

URL="https://automationexercise.com/"
Email_Field_XPATH="//input[@id='susbscribe_email']"
Submit_Email_XPATH="//button[@id='subscribe']"

#function for intializing the driver
def initialize_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

#funtion for URL
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

def scroll_to_footer(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    print("Scrolled to the footer.")
    time.sleep(3)

def enter_email_and_subscribe(driver,Email, Email_field_xpath, Submit_xpath):
    Email_Field=driver.find_element(By.XPATH,Email_field_xpath)
    Email_Field.clear()
    time.sleep(2)
    Email_Field.send_keys(Email)
    time.sleep(3)

    Email_Submit=driver.find_element(By.XPATH,Submit_xpath)
    Email_Submit.click()
    print("Email is entered and subscribed successfully!")
    time.sleep(3)

