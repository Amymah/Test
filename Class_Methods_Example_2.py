import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#Open Browser
#Click on "Contact Us"
#Use a 'static method' to validate the heading
#Use a 'class method' to track total form visits
#Use 'instance methods' for all actions
#Close the browser

class ContactPageTest:
    bas_url="https://automationexercise.com"
    conatct_visit_count=0

    def __init__(self):
        self.driver=webdriver.Chrome()

    #instance method
    def Open_Browser(self):
        self.driver.get(self.bas_url)
        self.driver.maximize_window()
        time.sleep(3)

    #instance method
    def Go_To_Contact_Page(self):
        Contact_Page=self.driver.find_element(By.XPATH,"//a[@href='/contact_us']")
        Contact_Page.click()
        time.sleep(3)
        return Contact_Page

    #instance method
    def Get_Contact_Heading(self):
        Contact_Heading=self.driver.find_element(By.XPATH,"(//div[@class='col-sm-8'])[2]//child::h2").text
        return Contact_Heading

    #Static method
    @staticmethod
    def Validate_Heading(text):
        if "GET IN TOUCH" in text.upper():
            print("Heading is correct.")
        else:
            print("Heading mismatched.")

    #class methos
    @classmethod
    def Increase_Contact_Count(cls):
        cls.conatct_visit_count += 1
        print(f"Contact Page visited: {cls.conatct_visit_count} time(s).")

    #instance method
    def Close_Browser(self):
        self.driver.quit()

def main():
    Contact=ContactPageTest()

    Contact.Open_Browser()
    Contact.Go_To_Contact_Page()

    heading_text=Contact.Get_Contact_Heading()

    ContactPageTest.Validate_Heading(heading_text)    #static method

    ContactPageTest.Increase_Contact_Count()          #class method

    Contact.Close_Browser()

    time.sleep(3)


if __name__ == "__main__":
    main()


class SauceDemoTest:
    base_url = "https://www.saucedemo.com"
    login_counter = 0

    def __init__(self):
        self.driver = webdriver.Chrome()

    #Instance method
    def open_login_page(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)

    #Instance method
    def login(self, username, password):
        Username=self.driver.find_element(By.ID, "user-name")
        Username.send_keys(username)
        time.sleep(3)
        Password=self.driver.find_element(By.ID, "password")
        Password.send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

    #Instance method: get page title
    def get_page_title(self):
        return self.driver.title

    #Static method
    @staticmethod
    def validate_title_contains(title, word):
        if word.lower() in title.lower():
            print("Title check passed")
        else:
            print("Title check failed")

    #Class method
    @classmethod
    def increment_login_counter(cls):
        cls.login_counter += 1
        print(f"Total successful logins: {cls.login_counter}")

    def close_browser(self):
        self.driver.quit()

def main():
    test = SauceDemoTest()

    test.open_login_page()
    test.login("standard_user", "secret_sauce")

    title = test.get_page_title()
    SauceDemoTest.validate_title_contains(title, "Swag Labs")  # Static method
    SauceDemoTest.increment_login_counter()  # Class method

    test.close_browser()

if __name__ == "__main__":
    main()



