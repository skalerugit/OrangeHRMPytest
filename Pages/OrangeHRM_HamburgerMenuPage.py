from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Locators.Locators import Locators
from Config.config import TestData
from time import sleep


class HamburgerMenuPage(BasePage):
    """By locators - OR"""
    INACTIVE_MENU_ITEMS = (By.CSS_SELECTOR,Locators.side_menu_items_inactive)
    USERNAME = (By.NAME, Locators.textbox_username_name)
    ACTIVE_MENU_ITEM = (By.CSS_SELECTOR, Locators.side_menu_item_active)
    BRAND_LOGO_IN_MENU = (By.CSS_SELECTOR, Locators.side_menu_brand_logo)
    TOGGLE_BTN_IN_MENU = (By.CSS_SELECTOR, Locators.side_menu_toggle_button)

    """Constructor of Login Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.APP_URL)

    def verify_inactive_list_menu_items(self):
        expected_list = ["Admin", "Leave", "Time", "Recruitment", "My Info", "Performance", "PIM",
                         "Directory", "Maintenance", "Buzz"]
        actual_list = self.get_elements_text(self.INACTIVE_MENU_ITEMS)
        assert expected_list == actual_list

    def verify_active_list_menu_item(self):
        return self.get_element_text(self.ACTIVE_MENU_ITEM)

    def verify_toggle_button_is_enabled(self):
        self.do_click(self.TOGGLE_BTN_IN_MENU)
        sleep(5)


