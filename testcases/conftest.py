import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request, browser):
    # Launch browser and open the application
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        #default is set to Chrome
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("http://jupiter.cloud.planittesting.com")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")