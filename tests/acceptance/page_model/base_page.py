from tests.acceptance.locators.base_page import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property  # щоб звертатися як до властивості,а не методу
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)