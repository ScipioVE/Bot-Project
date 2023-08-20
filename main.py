from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from credentials import EMAIL, PASSWORD
from definitions import region_code, stateORregion, gold_checker
import time
import os
import RR_Paths

# Get the base directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


CHROME_DRIVER = os.path.join(BASE_DIR + "\drivers\chromedriver.exe")

url = "https://rivalregions.com/"

driver = webdriver.Chrome(CHROME_DRIVER)

WAIT = WebDriverWait(driver, 10)


# Handler performs as a menu to make a action
def handle_choice():
    print(
        "Select Options:\n [1] Enable auto\n [2] Move to region\n [3] Ask for WP\n [4] Logout"
    )
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


def energy_recharge():
    gold_display = driver.find_element(By.XPATH, RR_Paths.gold_xpath)
    recharge_energy, gold_amount = gold_checker(
        gold_display.get_attribute("textContent")
    )

    if recharge_energy:
        try:
            storage_btn = driver.find_element(By.XPATH, RR_Paths.storage_xpath)
            storage_btn.click()
            time.sleep(2)
            gold_div = WAIT.until(
                EC.presence_of_all_elements_located((By.XPATH, RR_Paths.gold_div_xpath))
            )

            time.sleep(2)
            gold_div[0].click()
            time.sleep(2)
            print("trying click on produce btn...")
            storage_produce_btn = driver.find_element(
                By.XPATH, RR_Paths.storage_produce_xpath
            )
            storage_produce_btn.clear()
            time.sleep(5)
            print("sending keys...")
            storage_produce_btn.send_keys(str(gold_amount))
            time.sleep(5)
            produce_green_btn = WAIT.until(
                EC.presence_of_element_located((By.XPATH, RR_Paths.produce_green_btn))
            )
            produce_green_btn.click()
            WAIT

        except Exception as e:
            print("Error:", type(e).__name__, str(e))
    else:
        print(f" gold amount: {gold_amount}")


def enable_auto():
    try:
        energy_recharge()
        work_action = driver.find_element(By.XPATH, RR_Paths.work_xpath)
        work_action.click()

        automatic_mode_button = WAIT.until(
            EC.presence_of_element_located((By.XPATH, RR_Paths.automatic_mode_xpath))
        )

        try:
            if (
                automatic_mode_button.is_displayed()
                and automatic_mode_button.is_enabled()
            ):
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
        move_btn = WAIT.until(
            EC.presence_of_element_located((By.XPATH, RR_Paths.move_btn_xpath))
        )
        move_btn.click()
        time.sleep(5)

        dropdown_toggle = driver.find_element(By.XPATH, RR_Paths.dropdown_toggle_xpath)
        dropdown_toggle.click()

        WAIT
        # Find all the list items within the dropdown list
        dropdown_list = WAIT.until(
            EC.visibility_of_element_located((By.XPATH, RR_Paths.dropdown_list_xpath))
        )
        dropdown_items = dropdown_list.find_elements(
            By.XPATH, RR_Paths.dropdown_items_xpath
        )

        # Iterate through the list items and perform actions
        for item in dropdown_items:
            target_item = item.find_element(
                By.XPATH, './input[@class="dd-option-value"]'
            )
            hidden_value = target_item.get_attribute("value")

            if hidden_value == 1 or "1":
                driver.execute_script("arguments[0].click()", target_item)
        # Click the Blue move buttom
        confirm_move_btn = WAIT.until(
            EC.presence_of_element_located((By.XPATH, RR_Paths.confirm_move_btn_xpath))
        )
        confirm_move_btn.click()
        # Driver wait and then click the green move to buttom
        WAIT
        green_confirm_btn = WAIT.until(
            EC.presence_of_element_located((By.XPATH, RR_Paths.green_confirm_btn_xpath))
        )
        green_confirm_btn.click()
        time.sleep(5)

    except Exception as e:
        print("Error:", type(e).__name__, str(e))


def ask_only_for_wp():
    wp_input = input("Ingrese el url: ")

    wp_url = stateORregion(wp_input)

    time.sleep(3)

    driver.get(wp_url)
    time.sleep(1)
    driver.refresh()
    time.sleep(1)

    try:
        WAIT
        wp_btn = WAIT.until(
            EC.presence_of_element_located((By.XPATH, RR_Paths.wp_btn_xpath))
        )
        wp_btn.click()
    except Exception as e:
        print("Error:", type(e).__name__, str(e))


def logout():
    # Logic for Logout
    print("Logout?")
    input_cmd = input("y/n: ")
    if input_cmd == "y":
        header_setups = driver.find_element(By.XPATH, RR_Paths.header_setups_xpath)
        header_setups.click()
        time.sleep(5)
        logout_button = driver.find_element(By.XPATH, RR_Paths.logout_button_xpath)
        logout_button.click()
        time.sleep(5)
        driver.quit()


def main():
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        email_input = driver.find_element(By.XPATH, RR_Paths.email_xpath)
        password_input = driver.find_element(By.XPATH, RR_Paths.password_xpath)

        driver.execute_script("arguments[0].scrollIntoView();", email_input)

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)

        login_button = driver.find_element(By.XPATH, RR_Paths.login_xpath)
        login_button.click()
        handle_choice()

    except Exception as e:
        print("Error:", type(e).__name__, str(e))


if __name__ == "__main__":
    main()
