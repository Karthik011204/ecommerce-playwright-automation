class ProductPage:

    def __init__(self, page):
        self.page = page

    def add_product_to_cart(self):
        self.page.locator("a[href='/books']").first.click()
        self.page.wait_for_load_state("networkidle")

        self.page.locator("a[href='/computing-and-internet']").last.click()
        self.page.wait_for_load_state("networkidle")

        self.page.click("#add-to-cart-button-13")
        self.page.wait_for_selector(".bar-notification.success")

        print("Product Added To Cart")
