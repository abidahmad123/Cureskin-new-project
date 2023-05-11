from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Amazon main page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('search for cart')
def search_amazon(context):
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("cart")
