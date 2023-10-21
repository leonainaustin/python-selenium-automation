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
driver.get('https://www.amazon.com/')

# locators
# amazon logo
# driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# email field
# driver.find_element(By.XPATH, "//input[@type='email']")
# continue button
# driver.find_element(By.ID, 'continue')
# conditions of use link
# driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# privacy notice link
# driver.find_element((By.XPATH, "//a[text()='Privacy Notice']"))
# need help link
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# forgot your password link
# driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# other issuers with sign in link
# driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
# create your amazon account button
# driver.find_element((By.XPATH, "//a[@id='createAccountSubmit']"))

driver.find_element(By.XPATH, "//span[text()='& Orders']").click()
#check result
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1[@class= 'a-spacing-small']").text
assert expected_result == actual_result, f'Error.Expected text {expected_result} did not match actual {actual_result}'
print('Teast case passed')
driver.quit()
