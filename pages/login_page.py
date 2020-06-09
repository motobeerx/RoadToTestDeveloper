from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):

        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)

        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)

        register = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        register.click()

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_login_url()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), 'Login form is absent'

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL is incorrect'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is absent'


