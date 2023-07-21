from selenium.webdriver.common.by import By

from pages.base_page import page

class SearchResultsPage(page):
    RESULT_TEXT = (By.XPATH, "//span[@class='label'][normalize-space()='Shop by Product']")

    def verify_search_results(self):
        expected_results = '"Open Cureskin main page"'
        actual_result = self.driver.find.element(*self.RESULT_TEXT).text
        assert expected_results == actual_result, \
            f'Error! Expected {expected_result} bot got actual {actual_result}'