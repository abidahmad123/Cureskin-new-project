from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Search for {search_query}')
def search_for_product(context, search_query):
    context.app.search_results_page.search_for_product(search_query)


@then('Verify the results have spf')
def verify_search_result(context):

    expected_result = context.driver.find_element(By.CSS_SELECTOR, 'img[srcset*= "//cdn.shopify.com/s/files/1/0293/8775/1508/products/1_b"]').text
    context.app.search_results_page.verify_search_result(expected_result)
    sleep(5)
