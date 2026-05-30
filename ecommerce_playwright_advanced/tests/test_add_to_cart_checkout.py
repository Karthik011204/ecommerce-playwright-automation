import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.orders_page import OrdersPage
from utils.config import BASE_URL, EMAIL, PASSWORD
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.regression
def test_add_to_cart_checkout(page):

    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    logger.info("Website opened")

    login = LoginPage(page)
    login.login(EMAIL, PASSWORD)
    logger.info("User logged in")

    product = ProductPage(page)
    product.add_product_to_cart()
    logger.info("Product added to cart")

    cart = CartPage(page)
    cart.open_cart()
    cart.validate_price()
    logger.info("Cart price validated")

    checkout = CheckoutPage(page)
    checkout.complete_checkout()
    logger.info("Checkout completed")

    orders = OrdersPage(page)
    orders.open_orders()
    orders.verify_order_details()
    orders.go_home()
    orders.logout()
    logger.info("Order verified and user logged out")
