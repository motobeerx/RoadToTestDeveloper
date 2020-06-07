from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '[class="btn btn-default"]:nth-child(1)')


class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_STATUS = (By.CSS_SELECTOR, '#content_inner')
    NAME_OF_ADDED_SHIPMENT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) > .alertinner strong')
    PRICE_OF_ADDED_SHIPMENT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) > .alertinner strong')


class ProductPageLocators:
    ADD_IN_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SHIPMENT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SHIPMENT_NAME = (By.CSS_SELECTOR, '.product_main  h1')

