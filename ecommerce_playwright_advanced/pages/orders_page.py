class OrdersPage:

    def __init__(self, page):
        self.page = page

    def open_orders(self):
        self.page.click("a.account")
        self.page.click("text=Orders")
        self.page.wait_for_load_state("networkidle")
        print("Orders Page Opened")

    def verify_order_details(self):
        assert self.page.locator(".order-list").is_visible()

        order_text = self.page.locator(".order-list").inner_text()

        print("Order Details:")
        print(order_text)

        assert "Order Number" in order_text

    def go_home(self):
        self.page.click(".header-logo a")

    def logout(self):
        self.page.click("text=Log out")
