from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Best Sellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs')


#@when('Search for Best Sellers')
#def search_amazon(context):
    #context.driver.find_element(By.ID, 'nav_cs_bestsellers').click()


@then('Verify search results shown')
def verify_search_results(context):
    expected_results = 'Amazon Best Sellers'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '#zg_banner_text').text
    assert expected_results == actual_result, f'Expected {expected_results} but got {actual_result}'
