import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#Global variable
URL = "https://automationexercise.com"
Products_Page_XPATH="//a[text()=' Products']"

#function for intializing the driver
def initialize_driver():
    global driver   #globally defining a variable inside the function so it can use in other functions as well or anywhere in the script.
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)  #Local variable
    driver.maximize_window()
    return driver

#funtion for URL
def open_url(url):
    driver.get(url)
    driver.maximize_window()

# Function to open site and click "Products"
def click_on_products(Product_page_xpath):

    # Local variable to find and click the 'Products' tab
    product_tab = driver.find_element(By.XPATH, Product_page_xpath)
    product_tab.click()
    print("Clicked on Products tab.")

    time.sleep(3)
    driver.quit()

def main():
    initialize_driver()
    open_url(URL)

    click_on_products(Products_Page_XPATH)
    driver.quit()

if __name__ == "__main__":
    main()