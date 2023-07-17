from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open cureskin main page')
def open_cureskin(context):
    context.driver.get('https://shop.cureskin.com/')
@when('Search for Shop by Product')
def search_cureskin(context):
    context.driver.find_element(By.XPATH, "//span[@class='label'][normalize-space()='Shop by Product']").click()
