from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    def add_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        shipment_price = self.get_shipment_price()
        shipment_name = self.get_shipment_name()
        button.click()
        WebDriverWait(self.browser, 3).until(ec.alert_is_present())
        return shipment_price, shipment_name

    def get_shipment_price(self):
        return self.browser.find_element(*ProductPageLocators.SHIPMENT_PRICE).text

    def get_shipment_name(self):
        return self.browser.find_element(*ProductPageLocators.SHIPMENT_NAME).text

    def is_shipment_in_basket(self, price, name):
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME_OF_ADDED_SHIPMENT).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_OF_ADDED_SHIPMENT).text
        assert alert_name == name and alert_price == price, f'The "{name}" has not been added'
