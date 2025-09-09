import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Products:
    def __init__(self):
        self.driver=webdriver.Chrome()

    def Open_Website(self):
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(3)

    def Go_To_Products(self):
        Product_Page= self.driver.find_element(By.XPATH,"//a[@href='/products']")
        Product_Page.click()
        time.sleep(3)

    def Search_Product(self, Product_Name):
        Search_Box=self.driver.find_element(By.ID,"search_product")
        Search_Box.clear()
        Search_Box.send_keys(Product_Name)
        time.sleep(3)
        Search_btn=self.driver.find_element(By.ID,"submit_search")
        Search_btn.click()
        time.sleep(3)

    def Verify_Results(self):
        Result_Heading=self.driver.find_element(By.XPATH,"//h2[@class='title text-center']").text
        time.sleep(3)
        if "SEARCHED PRODUCTS" in Result_Heading:
            print("Searched product displayed!")
        else:
            print("Searched product not displayed!")

    def Close_Browser(self):
        self.driver.quit()

def main():
    Tshirt=Products()

    Tshirt.Open_Website()

    Tshirt.Go_To_Products()

    Tshirt.Search_Product("tshirt")

    Tshirt.Verify_Results()

    Tshirt.Close_Browser()

if __name__ == "__main__":
    main()
