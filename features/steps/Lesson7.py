from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
@when('Search for cart')
def search_amazon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
@then('Verify search results shown')
def verify_search_results(context):
    expected_results = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    print(expected_results)
    print(actual_result)
    assert expected_results == actual_result, f'Expected {expected_results} but got {actual_result}'