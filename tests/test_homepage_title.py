import pytest
from playwright.sync_api import Page, expect

# --- Test -> Verify the website's main page title ---

# I ask for 'page' (Playwright) and 'base_url' (my custom fixture).
def test_homepage_title(page: Page, base_url):
    
    # 1. The Action: Navigate to the URL
    page.goto(base_url)

    # 2. The Verification (Assert):
    # I define the expected title.
    expected_title = "Palato Digital – O sabor da inovação digital"
    
    # We use Playwright's 'expect', which verifies and waits automatically.
    expect(page).to_have_title(expected_title)