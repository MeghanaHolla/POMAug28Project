from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class HomePage(BasePage):
    logout_link = (By.LINK_TEXT, "Log out")
    books_link = (By.PARTIAL_LINK_TEXT, "Books")

    def __init__(self, driver):
        super().__init__(driver)

    def isLogoutPresent(self):
        return self.isElement_present(self.logout_link)

    def click_BooksLink(self):
        self.do_click(self.books_link)

    def click_logout(self):
        self.do_click(self.logout_link)