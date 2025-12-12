import pytest
import re
from playwright.sync_api import Page, expect

# --- Test -> Services Page Navigation ---

def test_services_page_navigation(page: Page, base_url, layout):
    """
    Test Scenario: Verify navigation to the Services page and check its key content.
    
    Steps:
    1. Navigate to Homepage.
    2. Click 'Serviços' in the menu.
    3. Verify URL change.
    4. Verify specific Headings (H1 and Sub-heading).
    5. Verify First Service Card.
    6. Verify Header & Footer visibility.
    """

    # 1. Navigate to Homepage
    page.goto(base_url)

    # 2. Click 'Serviços'
    # using exact=False to handle potential whitespace (e.g. " Serviços ")
    page.get_by_role("link", name="Serviços", exact=False).first.click()

    # 3. Verify URL Check
    expect(page).to_have_url(re.compile(r".*/servicos/"))

    # 4. Verify Headings
    # 4.1 Main Heading (H1) -> 'Serviços'
    expect(page.get_by_role("heading", name="Serviços", exact=True)).to_be_visible()

    # 4.2 Sub-heading -> 'O que fazemos'
    # Inspecting the live site, this text is usually a span or a small heading above the simple H1.
    # We use get_by_text for specific content verification.
    expect(page.get_by_text("O que fazemos")).to_be_visible()

    # 5. Verify All Service Cards
    # We verify the presence of all 5 core services listed on the page.
    services = [
        "Estratégia e inovação digital",
        "Identidade e design da marca",
        "Desenvolvimento Web",
        "Alojamento e domínios",
        "Suporte e manutenção contínuos"
    ]

    for service in services:
        # Using exact=False to handle potential icons or extra whitespace
        expect(page.get_by_role("heading", name=service, exact=False).first).to_be_visible()

    # 6. Verify Layout (Header & Footer)
    # Header: Check for Logo and Menu
    layout.verify_header()

    # Footer: Check for a unique footer element or link
    # Using 'contentinfo' role which usually maps to the <footer> tag
    layout.verify_footer()
