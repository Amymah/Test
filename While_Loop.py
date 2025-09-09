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

# Setup for while loop
found = False
scroll_position = 0
scroll_step = 300
max_scrolls = 20
scrolls_done = 0

while not found and scrolls_done < max_scrolls:
    try:
        # Try to find the 'Subscription' heading
        heading = driver.find_element(By.XPATH, "//h2[text()='Subscription']")
        if heading.is_displayed():
            print("'Subscription' section is visible!")
            found = True
        else:
            raise Exception("Not visible yet")
    except:
        # Scroll down if not visible
        scroll_position += scroll_step
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        scrolls_done += 1
        time.sleep(1)

if not found:
    print("'Subscription' section was not found after scrolling.")

driver.quit()
