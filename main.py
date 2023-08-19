from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from credentials import EMAIL, PASSWORD
from regioncodes import region_code
import time
import os

# Get the base directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


CHROME_DRIVER = os.path.join(BASE_DIR + "\drivers\chromedriver.exe")

url = "https://rivalregions.com/"

driver = webdriver.Chrome(CHROME_DRIVER)

WAIT = WebDriverWait(driver,10)

# Handler performs as a menu to make a action
def handle_choice():
    print("Select Options:\n [1] Enable auto\n [2] Move to region\n [3] Ask for WP\n [4] Logout")
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1: 
            enable_auto()
        elif choice == 2:
            move_to_region()
        elif choice == 3:
            ask_only_for_wp()
        elif choice == 4:
            logout()
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a number.")

def enable_auto():
    try:

        work_xpath = "//div[@action='work' and @class='item_menu work_menu ajax_action header_menu_item tc']"
        work_action = driver.find_element(By.XPATH, work_xpath)
        work_action.click()

        automatic_mode_xpath = "//div[@class='work_w_autom button_red tip' and contains(text(), 'Automatic mode')]"

        automatic_mode_button = WAIT.until(EC.presence_of_element_located((By.XPATH, automatic_mode_xpath)))

        try: 
            if automatic_mode_button.is_displayed() and automatic_mode_button.is_enabled():
             automatic_mode_button.click()
             print("Automatic mode enabled successfully")
            else:
                print("Automatic mode still on")
        
        except NoSuchElementException:
            print("Something is wrong with the auto btn!")



        time.sleep(25)
   
    except Exception as e:
                print("Error:", type(e).__name__, str(e))

def move_to_region():
    # Logic for moving to a region
    url_input = input("Ingrese el url: ")
    region_url = f"https:///rivalregions.com/#map/details/{region_code(url_input)}"
    driver.get(region_url)
    time.sleep(2)
    driver.refresh()
    time.sleep(5)

    try:
        move_btn_xpath = "//div[@class='button_green region_details_move' and text()='Move here']"
        move_btn = WAIT.until(EC.presence_of_element_located((By.XPATH, move_btn_xpath)))
        move_btn.click()
        time.sleep(5)

        dropdown_toggle_xpath = '//div[@class="dd-selected"]'
        dropdown_toggle = driver.find_element(By.XPATH, dropdown_toggle_xpath)
        dropdown_toggle.click()

        WAIT
         # Find all the list items within the dropdown list
        dropdown_list_xpath = '//ul[@class="dd-options dd-click-off-close"]'
        dropdown_list = WAIT.until(EC.visibility_of_element_located((By.XPATH, dropdown_list_xpath)))

            
        dropdown_items_xpath = './li/a[@class="dd-option"]'
        dropdown_items = dropdown_list.find_elements(By.XPATH, dropdown_items_xpath)

         # Iterate through the list items and perform actions
        for item in dropdown_items:
         target_item = item.find_element(By.XPATH, './input[@class="dd-option-value"]')
         hidden_value = target_item.get_attribute('value')

    
         if hidden_value == 1 or '1':
           driver.execute_script("arguments[0].click()", target_item)



        confirm_move_btn_xpath = '//div[@id="move_here" and contains(@class, "button_blue map_d_b imp")]'
        confirm_move_btn = WAIT.until(EC.presence_of_element_located((By.XPATH, confirm_move_btn_xpath)))
        confirm_move_btn.click()
        WAIT
        time.sleep(2)
        green_confirm_btn_xpath = '//div[@id="move_here_ok" and contains(@class, "button_green map_d_b")]'
        green_confirm_btn = WAIT.until(EC.presence_of_element_located((By.XPATH, green_confirm_btn_xpath)))
        green_confirm_btn.click()

        time.sleep(10) 


    
    except Exception as e:
        print("Error:", type(e).__name__, str(e))

def ask_only_for_wp():
    # Logic for asking only for WP
    pass

def logout():
    # Logic for Logout
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

        time.sleep(5)  # You might want to add a delay here if necessary
        
        driver.quit()

def main():
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

        handle_choice()
    
    except Exception as e:
        print("Error:", type(e).__name__, str(e))

if __name__ == "__main__":
    main()