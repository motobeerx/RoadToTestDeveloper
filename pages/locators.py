from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_IN_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_NAME_OF_ADDED_SHIPMENT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) > .alertinner strong')
    ALERT_PRICE_OF_ADDED_SHIPMENT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) > .alertinner strong')
    SHIPMENT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SHIPMENT_NAME = (By.CSS_SELECTOR, '.product_main  h1')
