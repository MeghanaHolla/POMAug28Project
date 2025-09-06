import xlrd

from configurations.configs import TestData
from pages.HomePage import HomePage
from pages.LandingPage import LandingPage
from pages.RegistrationPage import RegistrationPage
from testScripts.conftest import BaseTest


class Test_VerifyRegistration(BaseTest):
    def test_verifyRegistration(self):
        self.landing = LandingPage(self.driver)
        self.reg = RegistrationPage(self.driver)
        self.home = HomePage(self.driver)

        workbook = xlrd.open_workbook("D:\\Training\\Training_Aug5\\TestData1.xls")
        sheet = workbook.sheet_by_name("Sheet1")
        rowCount = sheet.nrows
        for i in range(1, rowCount):
            self.landing.clickRegisterLink()
            fname = sheet.cell_value(i, 0)
            lname = sheet.cell_value(i, 1)
            email = sheet.cell_value(i, 2)
            password = sheet.cell_value(i, 3)
            self.reg.createnewAccount(fname, lname, email, password)
            actualMsg = self.reg.getSuccessMessage()
            assert "Your registration completed" in actualMsg
            self.driver.get(TestData.BASE_URL)
            self.home.click_logout()