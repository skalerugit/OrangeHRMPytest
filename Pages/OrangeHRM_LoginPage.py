from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Locators.Locators import Locators
from Config.config import TestData


class LoginPage(BasePage):

    """By locators - OR"""
    USERNAME = (By.NAME, Locators.textbox_username_name)
    PASSWORD = (By.NAME, Locators.textbox_password_name)
    LOGIN_BUTTON = (By.CSS_SELECTOR, Locators.button_login_css)
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, Locators.link_forgot_password_css)
    INVALID_ERROR_TEXT = (By.CSS_SELECTOR, Locators.error_invalid_login_css)
    COPYRIGHT_INFO = (By.CSS_SELECTOR, Locators.copyright_info_css)
    FORM_HEADER = (By.TAG_NAME, Locators.form_header)

    """Constructor of Login Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.APP_URL)

    """Page Actions"""

    """To Get the Login Page Title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """To check Forgot Password Link is visible"""
    def is_forgot_password_link_visible(self):
        return self.is_visible(self.FORGOT_PASSWORD_LINK)

    """To Login to the OrangeHRM"""
    def do_login(self, username, password):
        self.do_input_values(self.USERNAME, username)
        self.do_input_values(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    """To capture the error notification"""
    def get_error_notification(self):
        return self.get_element_text(self.INVALID_ERROR_TEXT)

    """To Clear the UserName and Password"""
    def clear_values(self):
        self.clear_input_value(self.USERNAME)
        self.clear_input_value(self.PASSWORD)

    """To capture the copyright information"""
    def get_copyright_information(self):
        return self.get_element_text(self.COPYRIGHT_INFO)

    """To capture the Form name"""
    def get_login_form_name(self):
        return self.get_element_text(self.FORM_HEADER)





