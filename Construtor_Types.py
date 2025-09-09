import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

URL="https://automationexercise.com"
class DefautlConstructor:
    def __init__(self):   #Default Constructor
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        print(URL)
        time.sleep(2)
        self.search_product()

    def search_product(self):   #Default Constructor
        #Go to Product Section
        Product_Page = self.driver.find_element(By.XPATH, "//a[@href='/products']")
        Product_Page.click()
        time.sleep(3)
        #Search Product
        search_box = self.driver.find_element(By.ID, "search_product")
        search_box.send_keys("T-shirt")
        time.sleep(3)
        Search_btn= self.driver.find_element(By.ID, "submit_search")
        Search_btn.click()
        time.sleep(3)
        print("Search executed")

class ParameterizedConstructor:
    def __init__(self, url, Product_Name):   #parameterized constructor
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Opened website: {url} using Parameterized Constructor")
        time.sleep(2)
        self.search_product(Product_Name)

    def search_product(self,product):
        Product_Page = self.driver.find_element(By.XPATH, "//a[@href='/products']")
        Product_Page.click()
        time.sleep(3)
        Search_Box= self.driver.find_element(By.ID, "search_product")
        Search_Box.send_keys(product)
        time.sleep(3)
        Search_Btn= self.driver.find_element(By.ID, "submit_search")
        Search_Btn.click()
        time.sleep(3)
        print(f"Searched for: {product} using Parameterized Constructor")
        time.sleep(2)
        self.driver.quit()

class OverloadedConstructor:
    def __init__(self, url="https://automationexercise.com", product="Dress"):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Opened website: {url} using Simulated Overloading Constructor")
        time.sleep(2)
        self.search_product(product)

    def search_product(self, product):
        Product_Page = self.driver.find_element(By.XPATH, "//a[@href='/products']")
        Product_Page.click()
        time.sleep(3)
        Search_Box = self.driver.find_element(By.ID, "search_product")
        Search_Box.send_keys(product)
        time.sleep(3)
        Search_Btn = self.driver.find_element(By.ID, "submit_search")
        Search_Btn.click()
        time.sleep(3)
        print(f"Searched for: {product} using Overloading Constructor")
        time.sleep(2)
        self.driver.quit()

def main():
    print("------ Default Constructor Execution ------")
    obj1 = DefautlConstructor()

    # 2. Parameterized Constructor
    print("------ Parameterized Constructor Execution ------")
    obj2 = ParameterizedConstructor("https://automationexercise.com", "Jeans")

    # 3. Overloaded Constructor
    print("------ Overloaded Constructor Execution ------")
    obj3 = OverloadedConstructor(product="Skirt")

if __name__ == "__main__":
    main()