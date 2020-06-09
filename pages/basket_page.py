from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        basket_status = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        assert 'Your basket is empty.' in basket_status, 'Basket is not empty'

    def message_should_disappear(self):
        assert self.is_disappeared(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT), 'Success message disappeared'

    def should_not_be_success_messsage_after_added_shipment(self):
        assert self.is_not_element_present(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT), \
            'Success message of adding in basket is presented'
