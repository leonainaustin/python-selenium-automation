from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given ("Open  Circle page")
def open_circle(context):
    context.app.circle_page.open_circle()


@then("Verify that clicking though Circle tabs works")
def verify_can_click_tabs(context):
    context.app.circle_page.verify_can_click_tabs()

