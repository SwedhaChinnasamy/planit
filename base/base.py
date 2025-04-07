from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass():
    def __init__(self, driver):
        self.driver = driver

    def wait_till_clickable(self, type, locator):
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.element_to_be_clickable((type, locator)))

    def wait_until_element_present(self, type, locator):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.presence_of_element_located((type, locator)))