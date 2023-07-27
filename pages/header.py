from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
class Header(Page):

    SHOP_BY_PRODUCT = (By.XPATH, "//span[@class='label'][normalize-space()='Shop by Product']")
    SUNSCREEN = (By.XPATH, "//span[@class='label'][normalize-space()='Sunscreens']")
    FIRST_PRODUCT = (By.XPATH, "//a[@class='card-information__text h4']")


    def click_shop_by_prod(self):
        self.click(*self.SHOP_BY_PRODUCT)
        sleep(5)

    def click_sunscreen(self):
        self.click(*self.SUNSCREEN)
        sleep(5)

    def verify_first_product(self):
        actual_text = self.driver.find_element(*self.FIRST_PRODUCT).text
        assert actual_text == 'SPF30 Sunscreen', f'Expected but got {actual_text}'


