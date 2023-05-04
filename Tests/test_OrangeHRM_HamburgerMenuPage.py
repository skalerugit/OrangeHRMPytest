from Tests.test_base import BaseTest
from Pages.OrangeHRM_HamburgerMenuPage import HamburgerMenuPage
from Pages.OrangeHRM_LoginPage import LoginPage
from Config.config import TestData
import time


class Test_HamburgerMenuPage(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(10)

    def test_get_inactive_menu_items_list(self):
        self.hamburgerMenuPage = HamburgerMenuPage(self.driver)
#         self.hamburgerMenuPage.verify_inactive_list_menu_items()

    def test_get_active_menu_item(self):
        self.hamburgerMenuPage = HamburgerMenuPage(self.driver)
        active_link = self.hamburgerMenuPage.verify_active_list_menu_item()
        assert active_link == TestData.ACTIVE_MENU_ITEM

    def test_toggle_button_is_closed(self):
        self.hamburgerMenuPage = HamburgerMenuPage(self.driver)
        self.hamburgerMenuPage.verify_toggle_button_is_enabled()
