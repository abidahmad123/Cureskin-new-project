from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
def browser_init(context):
    """
    :param context: Behave context
    """
    gecko_driver_path = GeckoDriverManager().install()
    driver = webdriver.Firefox(executable_path=gecko_driver_path)
    context.driver = driver
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
def before_step(context, step):
    print('\nStarted step: ', step)
def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()