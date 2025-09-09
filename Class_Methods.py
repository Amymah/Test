import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


#Instance Method --> it belongs to the object of the class
#--> it uses "self" to access instance variables
#--> call it using object name

#Static Method --> it belongs to the class, not to the object
#--> it does not use self
#--> it is used for helper functions
#--> Decorated with @staticmethod

#Class Mehtod --> Belongs to class not object
#--> uses @classmethod decorator
#--> Take cls as the first parameter

class Methods:
    base_url = "https://automationexercise.com"
    #Construtor
    def __init__(self):
        self.driver=webdriver.Chrome()

    #instance method
    def Open_Site(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)

    # instance method
    def Get_Title(self):
        return self.driver.title

    #Static Method
    @staticmethod
    def Verify_Title(title):
        if "Automation" in title:
            print("Title verified!")
        else:
            print("Title is not verified!")

    #class method
    @classmethod
    def Print_Baae_URL(cls):
        #class method using class variable
        print(f"Running test case on: {cls.base_url}")


    # instance method
    def Close_Browser(self):
        self.driver.quit()

def main():
    obj=Methods()

    obj.Open_Site()

    title= obj.Get_Title()

    Methods.Verify_Title(title)

    Methods.Print_Baae_URL()

    obj.Close_Browser()

if __name__ == "__main__":
    main()




