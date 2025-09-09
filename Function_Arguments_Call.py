from Function_Arguments import *
from selenium.webdriver.common.by import By

def main():
    driver=initialize_driver()

    open_url(driver,URL)

    Search_Product(driver, "tshirt",Search_BOX_ID)                   #Positional + defaults
    Search_Product(driver, "jeans", Search_BOX_ID,2)        #Positional + one optional
    Search_Product(driver, "dress",Search_BOX_ID, wait_time=3)       #Mix of positional + keyword
    Search_Product(driver, "top",Search_BOX_ID, Locator_Type=By.ID)  #Keyword

    driver.quit()

if __name__ == "__main__":
    main()