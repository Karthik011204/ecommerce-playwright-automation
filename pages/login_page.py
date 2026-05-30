class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, email, password):
        self.page.click("text=Log in")
        self.page.fill("#Email", email)
        self.page.fill("#Password", password)
        self.page.click("input[value='Log in']")

    def logout(self):
        self.page.click("text=Log out")
