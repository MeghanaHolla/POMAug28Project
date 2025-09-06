from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self, driver):
        #newnewnew
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def do_sendKeys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def do_getText(self, by_locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(by_locator)).text

    def isElement_present(self, by_locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(by_locator)).is_displayed()
