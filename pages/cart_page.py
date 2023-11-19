from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class CartPage(Page):
    HEADER = (By.CSS_SELECTOR, 'h1[class*= "styles__StyledHeading"]')

    def verify_cart_empty(self):
        expected = "Your cart is empty"
        actual = self.find_element(*self.HEADER).text
        assert expected == actual, f'Expected {expected} not match actual {actual}'

