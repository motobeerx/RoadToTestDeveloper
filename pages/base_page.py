from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocators
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    @staticmethod
    def get_fake_email():
        return str(time.time()) + "@fakemail.org"

    @staticmethod
    def get_fake_password():
        return int(time.time())

    def go_to_link(self, how, what):
        link = self.browser.find_element(how, what)
        assert ec.element_to_be_clickable(link), "Link is not clickable"
        link.click()
        return BasePage(self.browser, link)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
