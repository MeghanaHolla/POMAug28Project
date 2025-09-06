from pages.HomePage import HomePage
from pages.LandingPage import LandingPage
from pages.LoginPage import LoginPage
from testScripts.conftest import BaseTest

class Test_verifyLogin(BaseTest):
    def test_verifyLogin(self):
        self.landing = LandingPage(self.driver)
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)

        self.landing.clickLoginLink()
        self.login.application_login("meghanah123@yopmail.com", "Abcd@123")
        isLogoutDisplayed = self.home.isLogoutPresent()
        assert isLogoutDisplayed == True
