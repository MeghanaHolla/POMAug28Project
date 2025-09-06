from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class BooksPage(BasePage):
    add_toCart = (By.CSS_SELECTOR, "input[value='Add to cart']")
    cart_quantity= (By.CSS_SELECTOR, "span[class='cart-qty']")

    def __init__(self, driver):
        super().__init__(driver)

    def clickAddToCart(self):
        self.do_click(self.add_toCart)

    def getCartQuantity(self):
        strCartQnty = self.do_getText(self.cart_quantity)
        strCartQnty = strCartQnty.replace("(","").replace(")", "")
        quantity = int(strCartQnty)
        return quantity