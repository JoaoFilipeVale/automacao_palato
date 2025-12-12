import pytest
import re
from playwright.sync_api import Page, expect

# --- Test -> About Page Navigation ---

def test_about_page_navigation(page: Page, base_url):
    """
    Test Scenario: Verify navigation to the About page and check its key content.
    
    Steps:
    1. Navigate to Homepage.
    2. Click 'Sobre' in the menu.
    3. Verify URL change.
    4. Verify H1 and Intro Text.
    5. Verify Philosophy Section and Cards.
    6. Verify Header & Footer visibility.
    """

    # 1. Navigate to Homepage
    page.goto(base_url)

    # 2. Click 'Sobre'
    # Using exact=False to be robust against whitespace or casing
    page.get_by_role("link", name="Sobre", exact=False).first.click()

    # 3. Verify URL Check
    expect(page).to_have_url(re.compile(r".*/sobre/"))

    # 4. Verify Main Content
    
    # 4.1 Check Main Heading (H1) -> 'O "Palato" por trás do Digital'
    # We use single quotes for the string wrapper to allow double quotes inside.
    # exact=False helps if there's surrounding whitespace.
    expect(page.get_by_role("heading", name='O "Palato" por trás do Digital', exact=False)).to_be_visible()

    # 4.2 Verify Intro Text
    # "O Palato Digital é o seu parceiro especialista..."
    # We locate by text containing the partial string.
    expect(page.get_by_text("O Palato Digital é o seu parceiro especialista")).to_be_visible()

    # 5. Verify Philosophy Section
    
    # 5.1 Verify Section Title "A nossa filosofia"
    # Inspecting finding showed this as visible text, possibly a heading or just strong text.
    expect(page.get_by_text("A nossa filosofia")).to_be_visible()

    # 5.2 Verify Philosophy Cards
    # Card 1: 'Parceiros, não fornecedores'
    expect(page.get_by_text("Parceiros, não fornecedores")).to_be_visible()

    # Card 2: 'Performance, não “moda”'
    # Note: The quotes around "moda" might vary (straight vs curly).
    # We can use regex to be safe or try strict string if copy-paste from source is exact.
    # Given the source prompt had “moda”, we use that.
    expect(page.get_by_text("Performance, não “moda”")).to_be_visible()

    # Card 3: 'Design, não decoração'
    expect(page.get_by_text("Design, não decoração")).to_be_visible()

    # 6. Verify Layout (Header & Footer)
    
    # Header: Check for Logo
    expect(page.locator("#logo").or_(page.locator(".custom-logo-link"))).to_be_visible()

    # Footer: Check for footer element or contentinfo
    expect(page.get_by_role("contentinfo").or_(page.locator("footer"))).to_be_visible()
