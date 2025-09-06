from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegistrationPage(BasePage):
    firstName_field = (By.ID, "FirstName")
    lastName_field = (By.ID, "LastName")
    emailID_field = (By.ID, "Email")
    password_field = (By.ID, "Password")
    confirmPassword_field = (By.ID, "ConfirmPassword")
    register_Btn = (By.ID, "register-button")
    registration_msg = (By.CSS_SELECTOR, "div[class='result']")

    def __init__(self, driver):
        super().__init__(driver)

    def createnewAccount(self, firstName, lastName, emailID, password):
        self.do_sendKeys(self.firstName_field, firstName)
        self.do_sendKeys(self.lastName_field, lastName)
        self.do_sendKeys(self.emailID_field, emailID)
        self.do_sendKeys(self.password_field, password)
        self.do_sendKeys(self.confirmPassword_field, password)
        self.do_click(self.register_Btn)

    def getSuccessMessage(self):
        return self.do_getText(self.registration_msg)