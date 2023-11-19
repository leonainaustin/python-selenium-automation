from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_ICON)
