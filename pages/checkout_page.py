class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def complete_checkout(self):
        self.page.check("#termsofservice")
        self.page.click("#checkout")
        self.page.wait_for_load_state("networkidle")

        # Billing Address - uses existing address
        self.page.locator("#billing-buttons-container input.button-1").click()
        self.page.wait_for_timeout(2000)

        # Shipping Address - uses existing address
        self.page.locator("#shipping-buttons-container input.button-1").click()
        self.page.wait_for_timeout(2000)

        # Shipping Method
        self.page.check("#shippingoption_0")
        self.page.locator("#shipping-method-buttons-container input.button-1").click()
        self.page.wait_for_timeout(2000)

        # Payment Method
        self.page.check("#paymentmethod_0")
        self.page.locator("#payment-method-buttons-container input.button-1").click()
        self.page.wait_for_timeout(2000)

        # Payment Info
        self.page.locator("#payment-info-buttons-container input.button-1").click()
        self.page.wait_for_timeout(2000)

        # Confirm Order
        self.page.locator("#confirm-order-buttons-container input.button-1").click()
        self.page.wait_for_timeout(3000)

        success_text = self.page.locator(".section.order-completed .title").inner_text()
        print("Order Status:", success_text)

        assert "successfully processed" in success_text.lower()

        print("Order Placed Successfully")
