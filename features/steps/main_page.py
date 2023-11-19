from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')
HEADER_LINKS = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"] a')


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()

@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span[class*="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]').click()
@when('From right wide navigation menu, click Sign In')
def navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR,'a[href="/account"][data-test="accountNav-signIn"]').click()

@then('Verify header is present')
def verify_header_present(context):
    context.driver.find_element(*HEADER)

@then('Verify header has {number} links')
def verify_header_links(context, number):
    number = int(number)
    links = context.driver.find_elements(*HEADER_LINKS)
    #always return[], [webelemetn1].it will not fail
    print(links)
    assert len(links) == number, f'Expectet {number} links, but got {len(links)}'

@when('Click on your cart')
def search_product(context):
    context.app.main_page.click_cart()



@then('Verify "Your cart is empty" text is shown')
def verify_search(context):
    context.app.cart_page.verify_cart_empty()
