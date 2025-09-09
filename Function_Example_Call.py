from Function_Example import *

def main():
    driver=initialize_driver()
    open_url(driver, URL)

    scroll_to_footer(driver)

    enter_email_and_subscribe(driver,"amymau@gmail.com",Email_Field_XPATH,Submit_Email_XPATH)

    driver.quit()

if __name__ == "__main__":
    main()