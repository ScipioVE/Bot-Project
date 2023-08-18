from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import EMAIL, PASSWORD
import time
import os

# Get the base directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHROME_DRIVER = os.path.join(BASE_DIR + "\drivers\chromedriver.exe")

url = "https://rivalregions.com/"

driver = webdriver.Chrome(CHROME_DRIVER)  

try:
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    email_xpath = "//input[@name='mail']"
    email_input = driver.find_element(By.XPATH, email_xpath)

    password_xpath = "//input[@name='p']"
    password_input = driver.find_element(By.XPATH, password_xpath)
    
    driver.execute_script("arguments[0].scrollIntoView();", email_input)
    
    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)

    login_xpath = "//input[@name='s']"
    login_button = driver.find_element(By.XPATH, login_xpath)
    login_button.click()
    
    # Add additional actions here, like logging in

   

except Exception as e:
    print("Error:", type(e).__name__, str(e))



finally:

    print("Logout?")
    input_cmd = input("y/n: ")
    if input_cmd == 'y':
        header_setups_xpath = "//div[@id='header_setups']"
        header_setups = driver.find_element(By.XPATH, header_setups_xpath)
        header_setups.click()

        time.sleep(5)

        logout_button_xpath = "//div[@class='button_green float_left setups_logout' and text()='Logout']"
        logout_button = driver.find_element(By.XPATH, logout_button_xpath)
        logout_button.click()
    # Add a delay before quitting the driver
    time.sleep(15)  
    driver.quit()