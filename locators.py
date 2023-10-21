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

driver.get('https://www.amazon.com/')

# search by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

# search by XPATH
driver.find_element(By.XPATH, "//input[@type='text']")
driver.find_element(By.XPATH, "//input[@type='submit']")

# search XPATH, multiple attribute
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute' and @value='Go']")
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute' and @value='Go' and @type='submit']")

# search XPATH, using text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# contains()
driver.find_element(By.XPATH, "//h2[contains(text(), 'Scary-good Halloween')]")
# from parent to child
driver.find_element(By.XPATH, "//div[@id= 'nav-main']//a[text()= 'Best Sellers']")