from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocators
from .url import Url
import time
import math
import pytest


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

    @staticmethod
    def get_promo_offer_links(xfail_offer_number):
        links = [Url.PREFIX_PROMO_URL + f'{i}' for i in range(10) if i != xfail_offer_number]
        xfail_offer_link = pytest.param(Url.PREFIX_PROMO_URL + str(xfail_offer_number),
                                        marks=pytest.mark.xfail(reason="mistake on page"))
        links.insert(xfail_offer_number, xfail_offer_link)
        return links

    def go_to_link(self, how, what):
        link = self.browser.find_element(how, what)
        assert ec.element_to_be_clickable(link), "Link is not clickable"
        link.click()

    def open(self):
        x = self.browser.get(self.url)
        print(type(x))

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
