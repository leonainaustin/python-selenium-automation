from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class CartPage(Page):
    HEADER = (By.CSS_SELECTOR, 'h1[class*= "styles__StyledHeading"]')
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        expected = "Your cart is empty"
        self.verify_text(expected, *self.HEADER)

    def open_cart(self):
        self.open_url('https://www.target.com/cart')

    def verify_cart_items(self, amount):
        summary= self.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in summary, f"Expected '{amount} item' not in {summary}"

    # def verify_product_name(self):
    #     expected=
    #     actual = self.find_element(*self.CART_ITEM_TITLE).text
    #     assert self.store_product_name == actual, f'Expected {self.product_name}, but got {actual}'


