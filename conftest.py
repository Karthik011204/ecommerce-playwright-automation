import os
import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS, BROWSER_NAME

@pytest.fixture()
def page(request):
    with sync_playwright() as p:
        browser_type = getattr(p, BROWSER_NAME)
        browser = browser_type.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()

        request.node.page = page

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = getattr(item, "page", None)

        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot captured: {screenshot_path}")
