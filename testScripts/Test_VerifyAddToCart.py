import time
from pages.BooksPage import BooksPage
from pages.HomePage import HomePage
from pages.LandingPage import LandingPage
from pages.LoginPage import LoginPage
from testScripts.conftest import BaseTest

class Test_VerifyAddToCart(BaseTest):
    def test_AddToCart(self):
        self.landing = LandingPage(self.driver)
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
        self.books = BooksPage(self.driver)

        self.landing.clickLoginLink()
        self.login.application_login("meghanah123@yopmail.com", "Abcd@123")
        self.home.click_BooksLink()
        beforeQuantity = self.books.getCartQuantity()
        self.books.clickAddToCart()
        time.sleep(5)
        afterQuantity = self.books.getCartQuantity()
        assert afterQuantity == beforeQuantity + 1
