from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
AMAZON_Privacy_Notice = (By.CSS_SELECTOR, "a.help-display-cond[href='https://www.amazon.com/privacy']")
@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
@given('Open Amazon T&C page')
def verify_amazon_TC_page(context):
    context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_page(context):
    privacy_link = context.driver.find_element(*AMAZON_Privacy_Notice)
    privacy_link.click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])
@then('Verify Amazon Privacy Notice page is opened')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".help-content h1").text
    expected_text = 'Amazon.com Privacy Notice'
    assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'
@then('User can close new window and switch back to original')
def close_new_switch_to_old(context):
    context.driver.switch_to.window(context.original_window)
    context.driver.close()