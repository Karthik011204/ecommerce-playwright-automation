import random
import pytest

from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.config import BASE_URL, PASSWORD
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
def test_register_login_logout(page):

    random_number = random.randint(1, 9999)
    email = f"test{random_number}@gmail.com"

    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    register = RegisterPage(page)
    register.open_register()
    register.register_user("Karthik", "Tester", email, PASSWORD)

    logger.info("Registration completed")

    page.click("input[value='Continue']")

    login = LoginPage(page)
    login.logout()

    logger.info("User logged out after registration")

    login.login(email, PASSWORD)

    logger.info("Registered user logged in successfully")
