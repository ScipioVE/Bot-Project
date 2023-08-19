# Automode Paths

work_xpath = "//div[@action='work' and @class='item_menu work_menu ajax_action header_menu_item tc']"
automatic_mode_xpath = "//div[@class='work_w_autom button_red tip' and contains(text(), 'Automatic mode')]"

# Move Region Paths
move_btn_xpath = "//div[@class='button_green region_details_move' and text()='Move here']"
dropdown_toggle_xpath = '//div[@class="dd-selected"]'
dropdown_list_xpath = '//ul[@class="dd-options dd-click-off-close"]'
dropdown_items_xpath = './li/a[@class="dd-option"]'
confirm_move_btn_xpath = '//div[@id="move_here" and contains(@class, "button_blue map_d_b imp")]'
green_confirm_btn_xpath = '//div[@id="move_here_ok" and contains(@class, "button_green map_d_b")]'

# Logout 

header_setups_xpath = "//div[@id='header_setups']"
logout_button_xpath = "//div[@class='button_green float_left setups_logout' and text()='Logout']"


# Login // Main

email_xpath = "//input[@name='mail']"
password_xpath = "//input[@name='p']"
login_xpath = "//input[@name='s']"