import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class AutomationExerciseTest:   #Creating a class
    def __init__(self):
        self.driver=webdriver.Chrome()

    def Open_Website(self):
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(3)

    def Verify_Homepage(self):
        title=self.driver.title
        print("Page Title:", title)
        if "Automation Exercise" in title:
            print("Home Page loaded successfully")
        else:
            print("Home Page title mismatch")

    def Go_To_Login(self):
        Login_Page=self.driver.find_element(By.XPATH,"//a[@href='/login']")
        Login_Page.click()
        time.sleep(3)

    def Verify_Login_Page(self):
        Login_Heading=self.driver.find_element(By.XPATH,"//h2[text()='Login to your account']")
        if Login_Heading == "Login to your account":
            print("Login page displayed")
        else:
            print("Login page is not displayed")

    def Close_Browser(self):
        self.driver.quit()

def main():
    Test=AutomationExerciseTest()    #Creating an object/ instance of a class

    Test.Open_Website()

    Test.Verify_Homepage()

    Test.Go_To_Login()

    Test.Verify_Login_Page()

    Test.Close_Browser()

if __name__ == "__main__":
    main()