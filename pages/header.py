from selenium.webdriver.common.by import By
from pages.base_page import page

class Header(page):
    SHOP_BY_PROD_BTN = (By.XPATH, "//span[@class='label'][normalize-space()='Shop by Product']")
    SUNSCREENS_BTN = (By.XPATH, "//span[@class='label'][normalize-space()='Sunscreens']")

    def search_for_product(self):
        self.input_text('Shop by Product', *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)


