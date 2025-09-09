import time
import os
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

URL="https://automationexercise.com/"
Contact_Us_XPATH="//a[@href='/contact_us']"
Name_XPATH="//input[@placeholder='Name']"
Email_XPATH="//input[@placeholder='Email']"
Subject_XPATH="//input[@placeholder='Subject']"
Message_XPATH="//textarea[@placeholder='Your Message Here']"
File_Upload_NAME="upload_file"
Submit_Btn_NAME="submit"
Success_Message_XPATH="//div[@class='status alert alert-success']"

class Constructors:
    #default constructor
    def __init__(self, Name="Amymah", Email="test@gmail.com", Subject="General Inquiry", Message="I am testing the contact form of this website."):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(3)

        self.name=Name
        self.email=Email
        self.subject=Subject
        self.message=Message

    #class method to stimulate constructor overloading
    @classmethod
    def With_Default_Values(cls):
        print("Using defalut values for contact form")
        return cls()


    #Fill form
    def Fill_Form(self, Contact_Us_xpath, Name_xpath, Email_xpath, Subject_xpath, Message_xpath, Upload_File_Name, Submit_Btn_Name):
        #go to Contact us page
        Contact_Us_Page=self.driver.find_element(By.XPATH,Contact_Us_xpath)
        Contact_Us_Page.click()
        time.sleep(5)

        Name_field=self.driver.find_element(By.XPATH,Name_xpath)
        Name_field.click()
        time.sleep(3)
        Name_field.send_keys(self.name)
        time.sleep(3)

        Email_field=self.driver.find_element(By.XPATH,Email_xpath)
        Email_field.click()
        time.sleep(3)
        Email_field.send_keys(self.email)
        time.sleep(3)

        Subject_field = self.driver.find_element(By.XPATH, Subject_xpath)
        Subject_field.click()
        time.sleep(3)
        Subject_field.send_keys(self.subject)
        time.sleep(3)

        Msg_field = self.driver.find_element(By.XPATH, Message_xpath)
        Msg_field.click()
        time.sleep(3)
        Msg_field.send_keys(self.message)
        time.sleep(3)

        #Upload file
        # file_path = os.path.expanduser("C:\\Users\\Amaima\\Documents\\Sample.txt")
        file_path = os.path.expanduser("C:\\Users\\Amaima\\OneDrive\\Documents\\Sample.txt")

        print("Uploading file from path:", file_path)

        if os.path.exists(file_path):
            upload = self.driver.find_element(By.NAME, Upload_File_Name)
            upload.send_keys(file_path)
            print("File uploaded successfully.")
        else:
            print(f"File does not exist at path: {file_path}")
            self.driver.quit()
            return

        #Submit Form
        Submit= self.driver.find_element(By.NAME,Submit_Btn_Name)
        Submit.click()
        time.sleep(3)

        #Handle alert
        Alert=self.driver.switch_to.alert
        Alert.accept()
        time.sleep(3)

    def Print_Success_msg(self, Msg_xpath):
        Message=self.driver.find_element(By.XPATH,Msg_xpath).text
        print(Message)

    def Close_Browser(self):
        self.driver.quit()

def main():

    print("--using parameterized constructor--")
    Form=Constructors("Ali","ali@gmail.com","Test subject","testing the form")
    Form.Fill_Form(Contact_Us_XPATH,Name_XPATH,Email_XPATH,Subject_XPATH, Message_XPATH, File_Upload_NAME,Submit_Btn_NAME)
    Form.Print_Success_msg(Success_Message_XPATH)
    Form.Close_Browser()

    print("\n--using default constructor--")
    Form2=Constructors()
    Form2.Fill_Form(Contact_Us_XPATH,Name_XPATH,Email_XPATH,Subject_XPATH,Message_XPATH, File_Upload_NAME,Submit_Btn_NAME)
    Form2.Print_Success_msg(Success_Message_XPATH)
    Form2.Close_Browser()

    print("\n--using overloaded constructor--")
    Form3=Constructors.With_Default_Values()
    Form3.Fill_Form(Contact_Us_XPATH,Name_XPATH,Email_XPATH,Subject_XPATH,Message_XPATH, File_Upload_NAME,Submit_Btn_NAME)
    Form3.Print_Success_msg(Success_Message_XPATH)
    Form3.Close_Browser()


if __name__ == "__main__":
    main()