import pytest
import re
from playwright.sync_api import Page, expect

# --- Test -> Full Contact Page Verification ---

def test_contact_full(page: Page, base_url):
    """
    Test Scenario: Full Contact Page End-to-End
    
    Steps:
    1. Navigate from Homepage (Header CTA).
    2. Verify URL.
    3. Verify Static Content (H2, Intro, Email).
    4. Execute Form Logic (Fill and Submit).
    """

    # 1. Navigation from Homepage
    page.goto(base_url)
    
    # Click 'Vamos falar' in the header
    # Using exact=False to match "Vamos falar" even with extra spaces
    page.get_by_role("link", name="Vamos falar", exact=False).first.click()

    # 2. Verify URL
    # Expect the URL to contain "/contacto/"
    expect(page).to_have_url(re.compile(r".*/contacto/"))
    
    # Wait for network idle to ensure scripts are loaded
    page.wait_for_load_state("networkidle")

    # 3. Static Content Verification
    
    # Check "Vamos falar"
    expect(page.get_by_role("heading", name="Vamos falar", exact=False).first).to_be_visible()

    # Check "Contacto"
    expect(page.get_by_text("Contacto", exact=False).first).to_be_visible()

    # Check Introductory Text (Partial match)
    # "Quer tenha uma ideia clara..."
    expect(page.get_by_text("Quer tenha uma ideia clara")).to_be_visible()

    # Check Email Address
    expect(page.get_by_text("geral@palatodigital.com")).to_be_visible()

    # 4. Form Execution (Adapted from test_contact_form.py)
    
    # Ensure form is ready
    name_field = page.locator('[name="your-name"]')
    name_field.scroll_into_view_if_needed()
    expect(name_field).to_be_visible()
    expect(name_field).to_be_editable()
    
    # Fill Name (Simulate typing to avoid JS reset issues)
    name_field.click()
    name_field.press_sequentially("Automated Test Playwright", delay=100)
    # Check value immediately
    # print(f"Name after typing: {name_field.input_value()}")
    
    # Fill Email
    email_field = page.locator('[name="your-email"]')
    expect(email_field).to_be_editable()
    email_field.click()
    email_field.press_sequentially("test@palatodigital.com", delay=50)
    
    # Fill Phone (even if optional, we test the field)
    phone_field = page.locator('[name="your-phone"]')
    expect(phone_field).to_be_editable()
    phone_field.click()
    phone_field.press_sequentially("932001002", delay=50)

    # Select Dropdown Option
    # Using select_option by label
    page.locator('[name="your-interest"]').select_option(value="Desenvolvimento Web")

    # Fill Message
    message_field = page.locator('[name="your-message"]')
    expect(message_field).to_be_editable()
    message_field.click()
    message_field.press_sequentially("This is an automated test message sent by a script during Sanity Test.", delay=10)

    # Check Acceptance Checkbox
    page.locator('[name="acceptance-policies"]').check()

    # Submit Form
    page.locator('input[type="submit"]').click()

    # Verify Submission Result (Expecting Error for this test scenario)
    expected_error_message = "Ocorreu um erro ao tentar enviar a sua mensagem. Por favor, tente novamente mais tarde."
    
    response_box = page.locator('.wpcf7-response-output')
    
    # Using contain_text as the message might have surrounding whitespace
    expect(response_box).to_contain_text(expected_error_message)
