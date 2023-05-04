import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.config import TestData
from selenium.webdriver.chrome.service import Service
from Utils.utility import utility
import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    print("initiating chrome driver")
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')  ## to avoid getting detected
    options.add_argument('headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.fixture
def utils():
    return utility
