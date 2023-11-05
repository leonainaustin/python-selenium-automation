from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')


@then('Verify Sign In form opened')
def verify_search(context):
    expected_result = "Sign into your Target account"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0.styles__AuthHeading-sc-kz6dq2-2.jhKFiw.kcHdEa').text
    assert expected_result == actual_result, f'Error. Expected_result {expected_result} did not match with actual_result {actual_result}'