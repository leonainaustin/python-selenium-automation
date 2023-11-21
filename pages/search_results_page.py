from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SearchResultsPage (Page):
    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT_TXT)

    def verify_search_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_add_to_cart (self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def store_product_name(self):
        self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME)

