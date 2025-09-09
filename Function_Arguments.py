import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#argument? --> provided while calling the function
#parameter? --> provided while declaring the function

URL="https://automationexercise.com"
Search_BOX_ID="search_product"
Search_ID= "submit_search"
Search_XPATH="//div[@class='productinfo text-center']//child::P"
Product_Page_XPATH="//a[@href='/products']"

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

#Function inculding all four types of the arguments
def Search_Product(driver, Product_Name,Search_Box_id, wait_time=3, Locator_Type=By.ID):
    """
        driver          - Required Positional
        product_name    - Required Positional
        wait_time       - Optional with default value
        locator_type    - Optional with default value
        search_box_id   - Keyword argument (named only)
        """

    #Go to the product page
    Product_Page=driver.find_element(By.XPATH,Product_Page_XPATH)
    Product_Page.click()
    time.sleep(wait_time)

    print(f"Searching for {Product_Name} with wait {wait_time} using locator {Locator_Type}.")
    time.sleep(wait_time)

    Search_Box=driver.find_element(Locator_Type,Search_Box_id)
    Search_Box.clear()
    Search_Box.send_keys(Product_Name)
    time.sleep(wait_time)
    Search=driver.find_element(By.ID,Search_ID)
    Search.click()
    time.sleep(wait_time)
    Results = driver.find_element(By.XPATH, Search_XPATH)
    driver.execute_script("arguments[0].scrollIntoView(true);", Results)
    time.sleep(wait_time)



