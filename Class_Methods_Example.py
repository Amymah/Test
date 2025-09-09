import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class AutomationExerciseSearch:
    base_url = "https://automationexercise.com"
    search_count = 0

    def __init__(self):
        self.driver = webdriver.Chrome()

    # Instance method
    def open_homepage(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)

    # Instance method
    def go_to_products(self):
        self.driver.find_element(By.XPATH, "//a[@href='/products']").click()
        time.sleep(2)

    # Instance method
    def search_product(self, product_name):
        self.driver.find_element(By.ID, "search_product").send_keys(product_name)
        self.driver.find_element(By.ID, "submit_search").click()
        time.sleep(2)
        result_text = self.driver.find_element(By.XPATH, "//h2[@class='title text-center']").text
        return result_text

    # Static method
    @staticmethod
    def validate_search_result(result_text):
        if "SEARCHED PRODUCTS" in result_text.upper():
            print("Search result validated")
        else:
            print("Search result not found")

    # Class method
    @classmethod
    def update_search_counter(cls):
        cls.search_count += 1
        print(f"Total searches run: {cls.search_count}")

    def close_browser(self):
        self.driver.quit()


def main():

    test = AutomationExerciseSearch()

    test.open_homepage()
    test.go_to_products()

    result = test.search_product("Tshirt")
    AutomationExerciseSearch.validate_search_result(result)   # Static method
    AutomationExerciseSearch.update_search_counter()          # Class method

    test.close_browser()
    time.sleep(3)

if __name__ == "__main__":
    main()


