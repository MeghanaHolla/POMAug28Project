import pytest
from selenium import webdriver

from configurations.configs import TestData

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    web_driver.implicitly_wait(20)

    yield
    web_driver.close()
