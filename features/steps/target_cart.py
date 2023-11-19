from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given('Open target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')



@then('Click on add to cart first product')
def add_cart_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor14062461").click()
    sleep(3)

@then('Click on View cart and Check out')
def view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()
    sleep(2)
@then('Verify cart')
def verify_cart(context):

    expected_keyword = "1 item"
    #expected_keyword= int(expected_keyword)
    result = context.driver.find_element(By.CSS_SELECTOR, "[href*='#Order%20Summary%20$22.71%20total,%201%20item%20']")
    assert expected_keyword in result,f'Expected{expected_keyword} not in  {result}'

