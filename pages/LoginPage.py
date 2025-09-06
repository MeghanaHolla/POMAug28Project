from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    email_IDFiled = (By.ID, "Email")
    password_filed = (By.ID, "Password")
    login_button = (By.CSS_SELECTOR, "input[value='Log in']")

    def __init__(self, driver):
        super().__init__(driver)

    def application_login(self, emailID, password):
        self.do_sendKeys(self.email_IDFiled, emailID)
        self.do_sendKeys(self.password_filed, password)
        self.do_click(self.login_button)