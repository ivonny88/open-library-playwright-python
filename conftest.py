import pytest
from playwright.sync_api import sync_playwright
import os


@pytest.fixture
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false").lower() == "true"

        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()
