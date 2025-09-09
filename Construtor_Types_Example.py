import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from OOPS_Python_Selenium.Function_Arguments import Search_Product


#Defult Constructor
# class Car:
#     def __init__(self):
#         self.make="Toyota"
#         self.model="Corolla"
#         self.year=2025
#
#
# car=Car()
# print(car.make)
# print(car.model)
# print(car.year)
# print("\n")
#
# #Parameterized constructor
# class Pcar:
#     def __init__(self, make, model, year):
#         self.make=make
#         self.model=model
#         self.year=year
#
# pcar=Pcar("Honda","Civic",2022)
# print(pcar.make)
# print(pcar.model)
# print(pcar.year)

# class AutomationExercise:
#     #constructor: Default values simulate both default and parameterized use
#     def __init__(self, url="https://automationexercise.com", product="tshirt"):
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         time.sleep(3)
#         self.driver.get(url)
#         print(f"Opened: {url}")
#         time.sleep(3)
#         self.Search_Product(product)
#
#     def Search_Product(self, product):
#         try:
#             Product_Page = self.driver.find_element(By.XPATH, "//a[@href='/products']")
#             Product_Page.click()
#             time.sleep(3)
#             Search_Box = self.driver.find_element(By.ID, "search_product")
#             Search_Box.send_keys(product)
#             time.sleep(3)
#             Search_Btn = self.driver.find_element(By.ID, "submit_search")
#             Search_Btn.click()
#             time.sleep(3)
#         except Exception as e:
#             print("searched failed: ",e)
#         finally:
#             self.driver.quit()
#
# def main():
#
#     #using default constructor (no arguments passed)
#     print("----- Default Constructor Example -----")
#     obj1=AutomationExercise()
#
#     #using parameterized constructors (arguments passed)
#     print("----- Parameterized Constructor Example -----")
#     obj2= AutomationExercise("https://automationexercise.com", "jeans")
#
# if __name__ == "__main__":
#     main()


#Simulated Overloaded constructor
class Student:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "Unknown"
            self.age = "Not Provided"
        elif len(args) == 1:
            self.name = args[0]
            self.age = "Not Provided"
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            raise ValueError("Too many arguments passed...Constructor overloaded.")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# -----------------------
# Simulated Overloaded Constructor Calls
# -----------------------

student1 = Student()  # No arguments (Default values)
student1.display()

student2 = Student("Amyma")  # One argument (Name only)
student2.display()

student3 = Student("Usman", 22)  # Two arguments (Name and age)
student3.display()


