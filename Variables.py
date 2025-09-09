import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#Local variables--> only accessible inside the methods
#Class variables--> only accessible inside the class, outside the methods
#Global variables--> can accessible anywhere, outside the class and the methods

#Global variables
env="Staging"

class Variables:
    #class variable
    Base_URL = "https://www.saucedemo.com"
    Login_attempts = 0

    def __init__(self):
        self.driver=webdriver.Chrome()

    def Open_Site(self):
        #Local variable
        browser_title="Swag Labs"

        self.driver.get(self.Base_URL)
        self.driver.maximize_window()
        time.sleep(3)

        actual_title=self.driver.title
        # print(actual_title)
        if browser_title in actual_title:
            print("Correct page loaded.")
        else:
            print("Page title mismatched.")


    def Perform_Login(self):
        #Local variables
        username="standard_user"
        password="secret_sauce"

        Username = self.driver.find_element(By.ID, "user-name")
        Username.send_keys(username)
        time.sleep(3)
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        # Accessing and modifying class variable
        Variables.Login_attempts += 1
        print(f"Login attempts: {Variables.Login_attempts}")

        #Accessing global variable
        # global env
        print(f"Running in {env} environment.")


    def Close_Site(self):
        self.driver.quit()

def main():
    test=Variables()
    test.Open_Site()
    test.Perform_Login()
    test.Close_Site()
    print("Calling by class:", Variables.Base_URL)
    print("Calling by class:", Variables.Login_attempts)
    print("Calling by object:", test.Base_URL)
    print("Calling by object:", test.Login_attempts)
    print(env)

if __name__ == "__main__":
    main()


