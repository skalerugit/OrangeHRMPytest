import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.service import Service
from Utils.utility import utility
import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        print("INFO: initiating chrome driver")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        if platform.system() == "Linux":
            sleep(8)
            web_driver = webdriver.Remote('http://selenium:4444/wd/hub',
                                          desired_capabilities=DesiredCapabilities.CHROME)

        else:
            service = Service(TestData.CHROME_EXECUTABLE_PATH_FOR_MAC)
            web_driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = Service(TestData.FIREFOX_EXECUTABLE_PATH_FOR_MAC)
        web_driver = webdriver.Firefox(service=service)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    yield
    web_driver.close()
    web_driver.quit()


@pytest.fixture
def utils():
    return utility
