from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators
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

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
        page.open()
        name_and_price = (page.get_shipment_name(), page.get_shipment_price())
        page.add_in_basket()
        page.is_shipment_in_basket(*name_and_price)

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
        product_page.open()
        product_page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.go_to_link(*BasePageLocators.BASKET_LINK)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()


def test_guest_should_see_login_link_on_product_page(browser):
    link = Url.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = Url.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_link(*BasePageLocators.LOGIN_LINK)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', BasePage.get_promo_offer_links(7))
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    name_and_price = (product_page.get_shipment_name(), product_page.get_shipment_price())
    product_page.add_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_shipment_in_basket(*name_and_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.add_in_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_success_messsage_after_added_shipment()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, Url.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.add_in_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.message_should_disappear()
