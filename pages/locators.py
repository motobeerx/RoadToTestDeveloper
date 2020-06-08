from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '[class="btn btn-default"]:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class BasketPageLocators:
    BASKET_STATUS = (By.CSS_SELECTOR, '#content_inner')
    NAME_OF_ADDED_SHIPMENT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) > .alertinner strong')
    PRICE_OF_ADDED_SHIPMENT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) > .alertinner strong')


class ProductPageLocators:
    ADD_IN_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SHIPMENT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SHIPMENT_NAME = (By.CSS_SELECTOR, '.product_main  h1')

