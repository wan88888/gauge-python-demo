from getgauge.python import step, before_scenario, after_scenario
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from getgauge.python import data_store
from step_impl.pages.login_page import LoginPage

@before_scenario
def setup():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式运行
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    data_store.scenario.driver = driver
    data_store.scenario.login_page = LoginPage(driver)

@after_scenario
def teardown():
    driver = data_store.scenario.driver
    if driver:
        driver.quit()

@step('Navigate to login page')
def navigate_to_login_page():
    login_page = data_store.scenario.login_page
    login_page.navigate_to()

@step('Enter username <username>')
def enter_username(username):
    login_page = data_store.scenario.login_page
    login_page.enter_username(username)

@step('Enter password <password>')
def enter_password(password):
    login_page = data_store.scenario.login_page
    login_page.enter_password(password)

@step('Click login button')
def click_login_button():
    login_page = data_store.scenario.login_page
    login_page.click_login()

@step('Verify successful login message')
def verify_successful_login():
    login_page = data_store.scenario.login_page
    message = login_page.get_flash_message()
    assert 'You logged into a secure area!' in message, \
        f'Expected success message not found. Actual message: {message}'

@step('Verify failed login message')
def verify_failed_login():
    login_page = data_store.scenario.login_page
    message = login_page.get_flash_message()
    assert 'Your username is invalid!' in message, \
        f'Expected error message not found. Actual message: {message}'