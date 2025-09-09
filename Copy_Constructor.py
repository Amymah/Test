import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Person:
    def __init__(self, First_Name, Last_Name, Gender, Age):
        self.First_Name= First_Name
        self.Last_Name = Last_Name
        self.Gender = Gender
        self.Age = Age

    # Copy constructor
    @classmethod
    def copy(cls, person_data):
        return cls(person_data.First_Name, person_data.Last_Name, person_data.Gender,person_data.Age)

    def Display_Info(self,):
        print(f"First name: {self.First_Name}")
        print(f"Last name: {self.Last_Name}")
        print(f"Gender: {self.Gender}")
        print(f"Age: {self.Age}")


def main():

    person_obj=Person("Amymah","Usman","Female","23")
    person_obj.Display_Info()
    #copy of person object
    person_obj_copy=Person.copy(person_obj)
    print("\nPrinitng info with copy of the object:")
    print(person_obj_copy.First_Name, person_obj_copy.Last_Name,person_obj_copy.Gender,person_obj_copy.Age)


if __name__ == "__main__":
    main()