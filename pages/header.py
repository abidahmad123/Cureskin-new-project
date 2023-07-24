from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
class Header(Page):

    SHOP_BY_PRODUCT = (By.XPATH, "//span[@class='label'][normalize-space()='Shop by Product']")
    SUNSCREEN = (By.XPATH, "//span[@class='label'][normalize-space()='Sunscreens']")


    def click_shop_by_prod(self):
        self.click(*self.SHOP_BY_PRODUCT)
        sleep(5)

    def click_sunscreen(self):
        self.click(*self.SUNSCREEN)
        sleep(5)


