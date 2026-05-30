class CartPage:

    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.click("#topcartlink")

    def validate_price(self):
        self.page.wait_for_selector(".product-unit-price")
        cart_price = self.page.locator(".product-unit-price").inner_text()

        print("Cart Price:", cart_price)

        assert "10.00" in cart_price

        print("Price Validation Passed")
