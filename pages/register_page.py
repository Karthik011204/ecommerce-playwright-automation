class RegisterPage:

    def __init__(self, page):
        self.page = page

    def open_register(self):
        self.page.click("text=Register")

    def register_user(self, firstname, lastname, email, password):
        self.page.check("#gender-male")
        self.page.fill("#FirstName", firstname)
        self.page.fill("#LastName", lastname)
        self.page.fill("#Email", email)
        self.page.fill("#Password", password)
        self.page.fill("#ConfirmPassword", password)
        self.page.click("#register-button")
