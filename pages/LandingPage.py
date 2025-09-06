from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LandingPage(BasePage):
    login_link = (By.LINK_TEXT, "Log in")
    register_link = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        super().__init__(driver)

    def clickLoginLink(self):
        self.do_click(self.login_link)

    def clickRegisterLink(self):
        self.do_click(self.register_link)