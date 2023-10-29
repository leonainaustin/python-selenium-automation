#1 Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# #1.locators
# # amazon logo
# "i.a-icon.a-icon-logo"
# # create account
# "h1.a-spacing-small"
# # your name
# "#ap_customer_name"
# #email
# 'input[type="email"]'
# # password
# '#ap_password'
# # reenter the password:
# '#ap_password_check'
# # create your amazon account
# '#continue'
# # condition of use
# 'a[href*="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?"]'
# # privacy notice
# 'a[href*="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?"]'
# #sign in
# 'a.a-link-emphasis'

# 2
# Search for coffee
# Feature: Search Target
#
#   Scenario: User can search for a icon
#     Given Open target home page
#     When Search  for your cart
#     Then Verify search worked
#     And Verify search result text

# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @given('Open target home page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('Search for your cart')
# def search_product(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'image[href*="https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart"]').click()
#
#     sleep(6)
#
#
# @then('Verify search result text')
# def verify_search(context):
#     search_header = context.driver.find_element(By.CSS_SELECTOR, 'h1').text
#     assert 'Your cart is empty' in search_header, f'Expected text "Your cart is empty" not in {search_header}'

# 3
driver.find_element(By.CSS_SELECTOR, 'span[class*="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href="/account"][data-test="accountNav-signIn"]').click()
sleep (4)
expected_result = "Sign into your Target account"
actual_result = driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0.styles__AuthHeading-sc-kz6dq2-2.jhKFiw.kcHdEa').text
assert expected_result == actual_result, f'Error. Expected_result {expected_result} did not match with actual_result {actual_result}'
print('Test case passed')
driver.quit()
