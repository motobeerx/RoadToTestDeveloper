from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators, BasketPageLocators, BasePageLocators
from .pages.url import Url
import pytest


@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Url.LOGIN_PAGE_URL)
        page.open()
        page.register_new_user(page.get_fake_email(), page.get_fake_password())
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
        page.open()
        name_and_price = (page.get_shipment_name(), page.get_shipment_price())
        page.add_in_basket()
        page.is_shipment_in_basket(*name_and_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
        page.open()
        assert page.is_not_element_present(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT), \
            'Success message of adding in basket is presented'


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    page.open()
    page.go_to_link(*BasePageLocators.BASKET_LINK)
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_basket_empty(), 'Basket is not empty'


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_link(*BasePageLocators.LOGIN_LINK)
    assert page.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Registration form is absent'
    assert page.is_element_present(*LoginPageLocators.LOG_IN_FORM), 'Login form is absent'


@pytest.mark.skip
@pytest.mark.parametrize('link', [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}'
                                  for i in range(1)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    name_and_price = (page.get_shipment_name(), page.get_shipment_price())
    page.add_in_basket()
    page.is_shipment_in_basket(*name_and_price)


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    page.open()
    page.add_in_basket()
    assert page.is_not_element_present(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT),\
        'Success message of adding in basket is presented'


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    page.open()
    assert page.is_not_element_present(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT), \
        'Success message of adding in basket is presented'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    page.open()
    page.add_in_basket()
    assert page.is_disappeared(*BasketPageLocators.NAME_OF_ADDED_SHIPMENT), 'Success message disappeared'
