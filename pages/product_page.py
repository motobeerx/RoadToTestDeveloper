from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):

    PRODUCT_PAGE_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    def add_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        button.click()
        # Было актуально, когда была промо акция - теперь окно с квизом не вылазит
        # WebDriverWait(self.browser, 3).until(ec.alert_is_present())

    def get_shipment_price(self):
        return self.browser.find_element(*ProductPageLocators.SHIPMENT_PRICE).text

    def get_shipment_name(self):
        return self.browser.find_element(*ProductPageLocators.SHIPMENT_NAME).text

    def is_shipment_in_basket(self, name, price):
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME_OF_ADDED_SHIPMENT).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_OF_ADDED_SHIPMENT).text
        assert alert_name == name and alert_price == price, f'The "{name}" has not been added'
