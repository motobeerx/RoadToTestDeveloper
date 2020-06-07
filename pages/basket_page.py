from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        basket_status = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        return True if 'Your basket is empty.' in basket_status else False
