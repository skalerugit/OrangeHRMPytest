from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_input_values(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        element = WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def clear_input_value(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def get_elements_text(self, by_locator):
        actual_list = []
        item = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for i in range(len(item)):
            actual_list.append(item[i].text)
        return actual_list




