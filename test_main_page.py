from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.url import Url
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, Url.MAIN_PAGE_URL)
    page.open()
    page.go_to_link(*BasePageLocators.BASKET_LINK)
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_basket_empty(), 'Basket is not empty'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, Url.MAIN_PAGE_URL)
    page.open()
    page.go_to_link(*BasePageLocators.LOGIN_LINK)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, Url.MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()
