from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify benefit box is present')
def verify_benefit_Present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*=h-margin-section-t-spacing]")

@then('Verify benefit box has {number} links')
def benefit_box_links(context, number):
    number = int(number)
    links= context.driver.find_elements(By.CSS_SELECTOR, "[class*=styles__BenefitCard-sc-9mx6dj")
    assert len(links) == number, f'Expectet {number} links, but got {len(links)}'