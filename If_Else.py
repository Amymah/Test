import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()
time.sleep(2)

products_tab = driver.find_element(By.XPATH, "//a[text()=' Products']")

#if-else condition
if products_tab.is_displayed():
    print("Products tab is visible.")
    products_tab.click()
else:
    print("Products tab not found.")

driver.quit()
