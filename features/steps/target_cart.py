from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given('Open target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')



@then('Add a mug into cart')
def add_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor13891751").click()

@then('Click on the cart')
def cart_click(context):
    context.driver.find_element(By.CSS_SELECTOR, 'image[href*="https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart"]').click()
@then('Verify cart item {expected_keyword}')
def verify_cart(context, expected_keyword):

    expected_keyword = "1 item"
    result = context.driver.find_element(By.CSS_SELECTOR, "[class*=styles__CartSummarySpan-sc-odscpb-3]")
    assert expected_keyword in result,f'Expected{expected_keyword} not in {result}'