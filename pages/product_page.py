from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):

    def add_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        button.click()

    def get_shipment_name(self):
        return self.browser.find_element(*ProductPageLocators.SHIPMENT_NAME).text

    def get_shipment_price(self):
        return self.browser.find_element(*ProductPageLocators.SHIPMENT_PRICE).text

    def is_shipment_in_basket(self, name, price):
        alert_name = self.browser.find_element(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT).text
        alert_price = self.browser.find_element(*BasketPageLocators.PRICE_OF_ADDED_SHIPMENT).text
        assert alert_name == name and alert_price == price, f'The "{name}" has not been added'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT), \
            'Success message of adding in basket is presented'
