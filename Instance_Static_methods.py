import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

URL="https://automationexercise.com/"
Product_Page_XPATH="//a[@href='/products']"
Search_Bar_ID="search_product"
Search_Btn_ID="submit_search"
Cart_Btn_XPATH="(//div[@class='productinfo text-center']//following-sibling::a)[1]"

class InstanceStaticMehtods:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(3)

    #instance method (Search and add product to tehe cart)
    def Search_And_Cart_Product(self, Product_Page_xpath, Search_Bar_id, Product_Name, Search_btn_id, Cart_Btn_xpath):
        formatted_name=self.clean_prodcut_name(Product_Name)  #clalling static method

        #Click products page
        Product_Page = self.driver.find_element(By.XPATH, Product_Page_xpath)
        Product_Page.click()
        time.sleep(3)

        # Search product name
        Search_Bar = self.driver.find_element(By.ID, Search_Bar_id)
        Search_Bar.click()
        time.sleep(2)
        Search_Bar.send_keys(formatted_name)
        time.sleep(2)

        Search_btn = self.driver.find_element(By.ID, Search_btn_id)
        Search_btn.click()
        time.sleep(2)

        # Add first item to the cart
        Cart_Btn = self.driver.find_element(By.XPATH, Cart_Btn_xpath)
        time.sleep(3)
        Cart_Btn.click()
        time.sleep(2)

        print(f"{formatted_name} was searched and added to the cart.")

    #Staic method (clean, format product name)
    @staticmethod
    def clean_prodcut_name(name):
        return name.strip().lower()

    def close_browser(self):
        self.driver.quit()

def main():
    method=InstanceStaticMehtods()

    #instance method uses static method internally
    method.Search_And_Cart_Product(Product_Page_XPATH,Search_Bar_ID, "   TShirt   ",Search_Btn_ID,Cart_Btn_XPATH)    #tshirt will be searched

    #static method can also be called directly
    print(InstanceStaticMehtods.clean_prodcut_name("   Jeans   "))  #output: jeans

if __name__ == "__main__":
    main()


