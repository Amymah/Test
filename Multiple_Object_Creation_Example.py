import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

URL="https://automationexercise.com/"

class Login:
    def __init__(self):    #Simple Constructor   #__init__()	Auto-runs when class is called
        self.driver = webdriver.Chrome()
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def Go_To_Login_Page(self):
        Login_Page=self.driver.find_element(By.XPATH,"//a[@href='/login']")
        Login_Page.click()
        time.sleep(3)

    def login(self, email, password):   #Parameterized Constructor
        # Enter email
        self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)
        # Enter password
        self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys(password)
        # Click login
        self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
        time.sleep(3)

    def get_login_error(self):
        try:
            error = self.driver.find_element(By.XPATH, "//p[contains(text(),'incorrect')]").text
            return error
        except:
            return "Login Successful or error message not found"

    def Success_Login(self):
        try:
            Home_Page = self.driver.find_element(By.XPATH, "(//a[text()=' Logged in as '] | //b[text()='Amymah usman'])[1]").text
            return Home_Page
        except:
            return "Login Successful or Home page not found"

    def close(self):
        self.driver.quit()

def main():
    #Invalid Login
    User1=Login()
    User1.Go_To_Login_Page()
    User1.login("amyma123@gmail.com","abcd1234")
    print("User 1 Login Result:", User1.get_login_error())

    #Invalid Login
    User2=Login()
    User2.Go_To_Login_Page()
    User2.login("amymah122@gmail.com","123*!-")
    print("User 2 Login Result:", User2.get_login_error())

    #Valid Login
    User3=Login()
    User3.Go_To_Login_Page()
    User3.login("amymausman15@gmail.com","Bss@2025")
    print("User 3 Login Result:", User3.Success_Login())

    User1.close()
    User2.close()
    User3.close()

if __name__ == "__main__":
    main()
