from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com
driver.get('https://www.target.com/')

# Search for coffee
driver.find_element(By.ID, 'search').send_keys('coffee')
driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
sleep(6)  # wait for ads to disappear

# Verify search result
search_results_header = driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
assert 'coffee' in search_results_header, f'Expected text coffee not in {search_results_header}'

# click on the cart
driver.find_element(By.CSS_SELECTOR, 'image[href*="https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart"]').click()
sleep(4)

# verify search result
search_header = driver.find_element(By.CSS_SELECTOR, 'h1').text
assert 'Your cart is empty' in search_header, f'Expected text "Your cart is empty" not in {search_header}'

driver.quit()