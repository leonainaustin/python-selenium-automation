from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SIGNIN_BTN = (By.CSS_SELECTOR, 'span[class*="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    RIGHT_WIDE_SIGNIN_BTN = (By.CSS_SELECTOR, 'a[href="/account"][data-test="accountNav-signIn"]')

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_for_element_click(*self.CART_ICON)

    def click_signin(self):
        self.wait_for_element_click(*self.SIGNIN_BTN)

    def right_wide_menu_click_signin(self):
        self.wait_for_element_click(*self.RIGHT_WIDE_SIGNIN_BTN)
