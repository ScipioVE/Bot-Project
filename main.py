from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, email_xpath)))

    password_xpath = "//input[@name='p']"
    password_input = driver.find_element(By.XPATH, password_xpath)
    
    driver.execute_script("arguments[0].scrollIntoView();", email_input)
    
    email_input.send_keys("your_email@example.com")
    password_input.send_keys("your_password")
    # Add additional actions here, like logging in

   

except Exception as e:
    print("Error:", type(e).__name__, str(e))

finally:
    # Add a delay before quitting the driver
    time.sleep(15)  