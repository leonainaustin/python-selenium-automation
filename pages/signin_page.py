from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):
    SIGNIN_FORM = (By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0.styles__AuthHeading-sc-kz6dq2-2.jhKFiw.kcHdEa')

    def verify_signin_form_opened(self):
        expected = "Sign into your Target account"
        self.verify_text(expected, *self.SIGNIN_FORM)



