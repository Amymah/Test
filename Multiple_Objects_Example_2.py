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
View_Cart_XPATH="(//a[@href='/view_cart'])[2]"
Element_XPATH="//li[@class='active']"
Results_XPATH="//h2[@class='title text-center']"

class MultipleObjectsCreation:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(3)

    def Search_And_Cart_Product(self, Product_Page_xpath, Search_Bar_id, Product_Name, Search_btn_id, Cart_Btn_xpath):
        #Go to the product page
        Product_Page=self.driver.find_element(By.XPATH,Product_Page_xpath)
        Product_Page.click()
        time.sleep(3)

        #Search product name
        Search_Bar=self.driver.find_element(By.ID,Search_Bar_id)
        Search_Bar.click()
        time.sleep(2)
        Search_Bar.send_keys(Product_Name)
        time.sleep(2)

        Search_btn=self.driver.find_element(By.ID,Search_btn_id)
        Search_btn.click()
        time.sleep(2)

        #Add first item to the cart
        Cart_Btn=self.driver.find_element(By.XPATH,Cart_Btn_xpath)
        time.sleep(3)
        Cart_Btn.click()
        time.sleep(2)

    def Get_Results_Heading(self, Results_xpath):
        Results=self.driver.find_element(By.XPATH,Results_xpath).text
        return Results

    def View_Item_In_Cart(self, View_Cart_xpath, Element_xpath):
        Cart=self.driver.find_element(By.XPATH,View_Cart_xpath)
        time.sleep(3)
        Cart.click()
        time.sleep(3)
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located((By.XPATH,Element_xpath)))


    def Close_Browser(self):
        self.driver.quit()


def main():

    # #Multiple object creation

    User1=MultipleObjectsCreation()

    User1.Search_And_Cart_Product(Product_Page_XPATH, Search_Bar_ID, "tshirt", Search_Btn_ID, Cart_Btn_XPATH)
    print("User1 Search Result: ", User1.Get_Results_Heading(Results_XPATH))
    User1.View_Item_In_Cart(View_Cart_XPATH, Element_XPATH)

    User1.Close_Browser()

    User2=MultipleObjectsCreation()

    User2.Search_And_Cart_Product(Product_Page_XPATH, Search_Bar_ID, "jeans", Search_Btn_ID, Cart_Btn_XPATH)
    print("User2 Search Result: ", User2.Get_Results_Heading(Results_XPATH))
    User2.View_Item_In_Cart(View_Cart_XPATH, Element_XPATH)


    User2.Close_Browser()

    User3=MultipleObjectsCreation()

    User3.Search_And_Cart_Product(Product_Page_XPATH, Search_Bar_ID, "top", Search_Btn_ID, Cart_Btn_XPATH)
    print("User3 Search Result: ", User3.Get_Results_Heading(Results_XPATH))
    User3.View_Item_In_Cart(View_Cart_XPATH, Element_XPATH)


    User3.Close_Browser()

    # User1 = MultipleObjectsCreation()
    # User2 = MultipleObjectsCreation()
    # User3 = MultipleObjectsCreation()
    #
    # User1.Search_And_Cart_Product(Product_Page_XPATH, Search_Bar_ID, "tshirt", Search_Btn_ID, Cart_Btn_XPATH)
    # print("User1 Search Result: ", User1.Get_Results_Heading(Results_XPATH))
    # User1.View_Item_In_Cart(View_Cart_XPATH, Element_XPATH)
    #
    # User2.Search_And_Cart_Product(Product_Page_XPATH, Search_Bar_ID, "jeans", Search_Btn_ID, Cart_Btn_XPATH)
    # print("User2 Search Result: ", User2.Get_Results_Heading(Results_XPATH))
    # User2.View_Item_In_Cart(View_Cart_XPATH, Element_XPATH)
    #
    # User3.Search_And_Cart_Product(Product_Page_XPATH, Search_Bar_ID, "top", Search_Btn_ID, Cart_Btn_XPATH)
    # print("User3 Search Result: ", User3.Get_Results_Heading(Results_XPATH))
    # User3.View_Item_In_Cart(View_Cart_XPATH, Element_XPATH)
    #
    # User1.Close_Browser()
    # User2.Close_Browser()
    # User3.Close_Browser()


if __name__ == "__main__":
    main()



