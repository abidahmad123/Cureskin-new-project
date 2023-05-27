from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for Best Sellers')
def search_amazon(context):
    context.driver.find_element(By.ID, 'nav_cs_bestsellers').click()


@then('Verify search results shown')
def verify_search_results(context):
    expected_results = 'Amazon Best Sellers'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'a-size-extra-large a-color-base _p13n-zg-banner-landing-page-header_style_zgLandingPageBannerText__3HlJo')
    assert expected_results == actual_result, f'Expected {expected_results} but got {actual_result}'
