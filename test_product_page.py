from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, LoginPageLocators
import pytest


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    assert page.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Registration form is absent'
    assert page.is_element_present(*LoginPageLocators.LOG_IN_FORM), 'Login form is absent'


@pytest.mark.parametrize('link', [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}'
                                  for i in range(1)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    name_and_price = (page.get_shipment_name(), page.get_shipment_price())
    page.add_in_basket()
    page.solve_quiz_and_get_code()
    page.is_shipment_in_basket(*name_and_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.add_in_basket()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_NAME_OF_ADDED_SHIPMENT),\
        'Success message of adding in basket is presented'


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPage.PRODUCT_PAGE_URL)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_NAME_OF_ADDED_SHIPMENT), \
        'Success message of adding in basket is presented'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.add_in_basket()
    assert page.is_disappeared(*ProductPageLocators.ALERT_NAME_OF_ADDED_SHIPMENT), 'Success message disappeared'
