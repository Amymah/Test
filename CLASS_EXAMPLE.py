import time
import os
from os import times
from webbrowser import parse_args

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Global variable
site_name="Automation Exercise"
URL="https://automationexercise.com/"
Default_email="test@gmail.com"
Default_password= "12345"
Actual_email="amymausman15@gmail.com"
Actual_Password="Bss@2025"
Login_page_XPATH="//a[@href='/login']"
Email_NAME="email"
Password_NAME="password"
Login_btn_XPATH="//button[@data-qa='login-button']"
Logout_XPATH="//a[@href='/logout']"
Login_MSG="Login successfully!"
Logout_MSG="Logged out successfully!"
Expected_username= "Amymah usman"
Signup_Name_XPATH="//input[@data-qa='signup-name']"
Signup_Email_XPATH="//input[@data-qa='signup-email']"
Signup_btn_XPATH="//button[@data-qa='signup-button']"
#Acc info
Radio_btn_XPATH="//input[@id='id_gender2']"
Password_Field_XPATH="//input[@id='password']"
Days_Dropdown_XPATH="//select[@id='days']"
Day_XPATH= "(//option[@value='7'])[1]"
Months_Dropdown_XPATH="//select[@id='months']"
Month_XPATH= "(//option[@value='9'])[2]"
Years_Dropdown_XPATH="//select[@id='years']"
Year_XPATH= "//option[@value='2001']"
Checkbox_1_XPATH="//input[@id='newsletter']"
Checkbox_2_XPATH="//input[@id='optin']"
#Address info
First_Name_XPATH="//input[@id='first_name']"
Last_Name_XPATH="//input[@id='last_name']"
Company_XPATH="//input[@id='company']"
Address_XPATH="//input[@id='address1']"
Country_Dropdown_XPATH="//select[@id='country']"
Country_XPATH="//option[@value='United States']"
State_XPATH="//input[@id='state']"
City_XPATH="//input[@id='city']"
Zipcode_XPATH="//input[@id='zipcode']"
Mobile_XPATH="//input[@id='mobile_number']"
Create_acc_btn_XPATH="//button[@data-qa='create-account']"


class LoginAutomation:
    #class variable
    total_logins= 0
    total_logouts= 0

    #Constructor (Default, Parameterized, Overloaded simulated)
    def __init__(self, driver=None, email=None, password=None):     #python does not support overloading of constructor directly, so we can achieve it by initializing the parameters of the function by "None"
        if driver:
            self.driver=driver
        else:
            self.driver=webdriver.Chrome()

        self.url=URL
        self.email= email if email else Default_email
        self.password=password if password else Default_password


    #instance methos (works with object variables)
    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    #instance method
    def click_login_menu(self, Login_page_xpath):
        Login_btn=self.driver.find_element(By.XPATH,Login_page_xpath)
        time.sleep(3)
        Login_btn.click()
        time.sleep(3)

    # instance method
    def perform_login(self, email_name, password_name, login_btn_xpath):
        Email_field=self.driver.find_element(By.NAME,email_name)
        time.sleep(3)
        Email_field.click()
        Email_field.send_keys(self.email)
        time.sleep(3)

        Password_field = self.driver.find_element(By.NAME, password_name)
        time.sleep(3)
        Password_field.click()
        Password_field.send_keys(self.password)
        time.sleep(3)

        Login_btn=self.driver.find_element(By.XPATH,login_btn_xpath)
        time.sleep(3)
        Login_btn.click()
        time.sleep(3)

        LoginAutomation.total_logins += 1

        try:
            # Wait for the element with the expected username to appear
            Login = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//b[text()='{Expected_username}']"))
            )
            Actual_username = Login.text

            if Expected_username in Actual_username:
                print(f"{Login_MSG}, Welcome {Actual_username}")
            else:
                print("Login not successful!")

        except TimeoutException:
            print(" Login not successful! Username not found on page (invalid credentials).")
    #instance method
    def log_out(self, logout_xpath):
        Logout=self.driver.find_element(By.XPATH,logout_xpath)
        time.sleep(3)
        Logout.click()
        time.sleep(3)
        print(Logout_MSG)
        LoginAutomation.total_logouts += 1

    #class method (works with class variables)
    @classmethod
    def display_counts(cls):
        print(f"Total login attempts: {cls.total_logins}")
        print(f"Total logout attempts: {cls.total_logouts}")

    #static method (independent logic, doesn't use object or class data/variables)
    @staticmethod
    def site_motto():
        print("Site motto: Quality Automation Practice!")


class Signup:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(3)

    def Perform_signup(self, signup_page_xpath, signup_name_xpath, name, signup_email_xpath, email,  signup_btn_xpath):
        Signup_page=self.driver.find_element(By.XPATH,signup_page_xpath)
        time.sleep(3)
        Signup_page.click()
        time.sleep(2)

        name_field= self.driver.find_element(By.XPATH,signup_name_xpath)
        time.sleep(2)
        name_field.click()
        name_field.send_keys(name)

        email_field= self.driver.find_element(By.XPATH,signup_email_xpath)
        time.sleep(2)
        email_field.click()
        email_field.send_keys(email)

        Signup_btn= self.driver.find_element(By.XPATH,signup_btn_xpath)
        time.sleep(3)
        Signup_btn.click()
        time.sleep(3)
        print("Landed onto Account Information page successfully!")

    def account_info(self, radio_btn_xpath, password_xpath, password, day_dropdown_xpath, day_xpath, month_dropdown_xpath, month_xpath, year_dropdown_xpath, year_xpath, checkbox1_xpath, checkbox2_xpath):
        salutations= self.driver.find_element(By.XPATH,radio_btn_xpath)
        time.sleep(3)
        salutations.click()
        time.sleep(2)

        password_field= self.driver.find_element(By.XPATH,password_xpath)
        time.sleep(3)
        password_field.click()
        password_field.send_keys(password)

        Day_dropdown= self.driver.find_element(By.XPATH,day_dropdown_xpath)
        time.sleep(3)
        Day_dropdown.click()
        time.sleep(2)
        Day= self.driver.find_element(By.XPATH,day_xpath)
        time.sleep(2)
        Day.click()
        time.sleep(3)

        Month_dropdown = self.driver.find_element(By.XPATH, month_dropdown_xpath)
        time.sleep(3)
        Month_dropdown.click()
        time.sleep(2)
        Month = self.driver.find_element(By.XPATH, month_xpath)
        time.sleep(2)
        Month.click()
        time.sleep(3)

        Year_dropdown = self.driver.find_element(By.XPATH, year_dropdown_xpath)
        time.sleep(3)
        Year_dropdown.click()
        time.sleep(2)
        Year = self.driver.find_element(By.XPATH, year_xpath)
        time.sleep(2)
        Year.click()
        time.sleep(3)

        Checkbox_1 = self.driver.find_element(By.XPATH,checkbox1_xpath)
        time.sleep(3)
        Checkbox_1.click()
        time.sleep(2)

        Checkbox_2 = self.driver.find_element(By.XPATH, checkbox2_xpath)
        time.sleep(3)
        Checkbox_2.click()
        time.sleep(2)
        print("Account information of the user has been captured!")


    def address_info(self,first_name_xpath,first_name, last_name_xpath, last_name,  company_xpath, company, address_xpath, address, country_dropdown_xpath, country_xpath, state_xpath, state, city_xpath, city,  zipcode_xpath, zipcode, mobile_no_xpath, mobile, create_acc_btn_xpath):
        First_name= self.driver.find_element(By.XPATH,first_name_xpath)
        time.sleep(2)
        First_name.click()
        First_name.send_keys(first_name)
        time.sleep(3)

        Last_name = self.driver.find_element(By.XPATH, last_name_xpath)
        time.sleep(2)
        Last_name.click()
        Last_name.send_keys(last_name)
        time.sleep(3)

        Company = self.driver.find_element(By.XPATH, company_xpath)
        time.sleep(2)
        Company.click()
        Company.send_keys(company)
        time.sleep(3)

        Address = self.driver.find_element(By.XPATH, address_xpath)
        time.sleep(2)
        Address.click()
        Address.send_keys(address)
        time.sleep(3)

        Country_dropdown = self.driver.find_element(By.XPATH, country_dropdown_xpath)
        time.sleep(2)
        Country.click()
        time.sleep(3)

        Country= self.driver.find_element(By.XPATH,country_xpath)
        time.sleep(3)
        Country.click()
        time.sleep(2)

        State = self.driver.find_element(By.XPATH, state_xpath)
        time.sleep(2)
        State.click()
        State.send_keys(state)
        time.sleep(3)

        City = self.driver.find_element(By.XPATH, city_xpath)
        time.sleep(2)
        City.click()
        City.send_keys(city)
        time.sleep(3)

        Zipcode = self.driver.find_element(By.XPATH, zipcode_xpath)
        time.sleep(2)
        Zipcode.click()
        Zipcode.send_keys(zipcode)
        time.sleep(3)

        Mobile = self.driver.find_element(By.XPATH, mobile_xpath)
        time.sleep(2)
        Mobile.click()
        Mobile.send_keys(mobile)
        time.sleep(3)

        print("Address info of the user is captured successfully!")

        Create_acc_btn= self.driver.find_element(By.XPATH,create_acc_btn_xpath)
        time.sleep(3)
        Create_acc_btn.click()
        time.sleep(2)

        print("Account created successfully!")


    def close_browser(self):
        self.driver.quit()



# #Object using default constructor values
# Login1= LoginAutomation()
# Login1.open_website()
# Login1.click_login_menu(Login_page_XPATH)
# Login1.perform_login(Email_NAME, Password_NAME, Login_btn_XPATH)
# Login1.driver.quit()
#
# #Object using parameterized constructor
# Driver2= webdriver.Chrome()
# Login2= LoginAutomation(Driver2, Actual_email, Actual_Password)
# Login2.open_website()
# Login2.click_login_menu(Login_page_XPATH)
# Login2.perform_login(Email_NAME, Password_NAME, Login_btn_XPATH)
# Login2.log_out(Logout_XPATH)
# Login2.driver.quit()
#
# #calling class method
# LoginAutomation.display_counts()
#
# #calling static method
# LoginAutomation.site_motto()
#
# #Access global variables
# print(f"Testing website: {site_name}")

Signup_obj=Signup()
Signup_obj.Perform_signup(Login_page_XPATH,Signup_Name_XPATH,"Amymah",Signup_Email_XPATH,"amyma@gmail.com",Signup_btn_XPATH)
Signup_obj.account_info(Radio_btn_XPATH, Password_Field_XPATH,"Bss@2025",Days_Dropdown_XPATH, Day_XPATH, Months_Dropdown_XPATH, Month_XPATH,Years_Dropdown_XPATH,Year_XPATH, Checkbox_1_XPATH, Checkbox_2_XPATH)
Signup_obj.address_info(First_Name_XPATH, "Amymah",Last_Name_XPATH,"Rajpoot",Company_XPATH,"BSS", Address_XPATH,"233 A main, US",Country_Dropdown_XPATH, Country_XPATH,State_XPATH,"Oman",City_XPATH,"Oman",Zipcode_XPATH,"09756",Mobile_XPATH,"03248724628",Create_acc_btn_XPATH)
Signup_obj.close_browser()
