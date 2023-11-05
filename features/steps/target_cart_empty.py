from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search  for your cart')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, 'image[href*="https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart"]').click()

    sleep(6)


@then('Verify search result text')
def verify_search(context):
    search_header = context.driver.find_element(By.CSS_SELECTOR, 'h1').text
    assert 'Your cart is empty' in search_header, f'Expected text "Your cart is empty" not in {search_header}'
