import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

URL="https://automationexercise.com/"
class MultipleObjects:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2)

    def Search_Product(self, Product_Name):
        Product_Page = self.driver.find_element(By.XPATH, "//a[@href='/products']")
        Product_Page.click()
        time.sleep(3)
        Search_Box = self.driver.find_element(By.ID, "search_product")
        Search_Box.clear()
        Search_Box.send_keys(Product_Name)
        time.sleep(3)
        Search_btn = self.driver.find_element(By.ID, "submit_search")
        Search_btn.click()
        time.sleep(3)

    def Get_Results_Heading(self):
        Results=self.driver.find_element(By.XPATH, "//h2[@class='title text-center']").text
        return Results

    def Close(self):
        self.driver.quit()

def main():
    User1=MultipleObjects()
    User2=MultipleObjects()

    User1.Search_Product("tshirt")
    print("User1 search result: ",User1.Get_Results_Heading())

    User2.Search_Product("jeans")
    print("User2 search result: ", User2.Get_Results_Heading())

    User1.Close()
    User2.Close()


if __name__ == "__main__":
    main()



