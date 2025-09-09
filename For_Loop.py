import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch browser and open site
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()
time.sleep(2)

# Step 2: Click on 'Products' tab
products_tab = driver.find_element(By.XPATH, "//a[text()=' Products']")
products_tab.click()
time.sleep(3)

# Step 3: Find all product names
product_elements = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")

# Step 4: Use for loop to print product names
print("List of Products:\n")
for index, product in enumerate(product_elements, start=1): #to print the product name along with the index
    print(f"{index}. {product.text}")

# Step 5: Close browser
driver.quit()
