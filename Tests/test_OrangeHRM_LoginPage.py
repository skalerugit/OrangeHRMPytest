from Tests.test_base import BaseTest
from Pages.OrangeHRM_LoginPage import LoginPage
from Config.config import TestData


class Test_LoginPage(BaseTest):

    def test_forgot_password_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_forgot_password_link_visible()
        print(flag)

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_copyright_info(self):
        self.loginPage = LoginPage(self.driver)
        copyright_text = self.loginPage.get_copyright_information()
        if copyright_text != TestData.COPYRIGHT_YEAR:
            raise AssertionError("Copyright text does not match TestData.COPYRIGHT_YEAR")

    def test_form_header(self):
        self.loginPage = LoginPage(self.driver)
        form_header = self.loginPage.get_login_form_name()
        assert form_header == TestData.FORM_HEADER

    def test_invalid_login(self, utils):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(utils.generate_random_username(), utils.generate_random_password())
        error = self.loginPage.get_error_notification()
        assert error == TestData.INVALID_LOGIN_TEXT

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.clear_values()
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)




