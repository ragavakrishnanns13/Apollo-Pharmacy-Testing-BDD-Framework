import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
from utilities.logger import setup_logger

@pytest.fixture()
def setup():
    # Pytest fixture to initialize and configure the Selenium WebDriver.
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    configobj = ConfigReader()
    url = configobj.get_url()
    driver.get(url)

    yield driver

    driver.quit()








