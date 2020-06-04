from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('link',
                         [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}'
                          for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    price_and_name = page.add_in_basket()
    page.solve_quiz_and_get_code()
    page.is_shipment_in_basket(*price_and_name)
