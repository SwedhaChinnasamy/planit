import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request, browser):
    # Launch browser and open the application
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser =="edge":
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()
        #print("Please provide valid browser. Supported browser values are 'chrome', 'firefox' or 'edge")
    driver.maximize_window()
    driver.get("http://jupiter.cloud.planittesting.com")
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")