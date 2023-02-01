import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.firefox.options import Options

options=Options()
options.binary_location = r"C:/Drivers/geckodriver.exe"
FIREFOX_EXECUTABLE_PATH = "C:/Drivers/geckodriver"


@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param=="chrome":
        web_driver=webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)

    if request.param=="firefox":
        web_driver=webdriver.Firefox(options=options, executable_path=TestData.FIREFOX_EXECUTABLE_PATH)

    request.cls.driver=web_driver
    yield
    web_driver.close()