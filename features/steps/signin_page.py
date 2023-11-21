from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')


@then('Verify Sign In form opened')
def verify_signin_form_opened(context):
    context.app.signin_page.verify_signin_form_opened()