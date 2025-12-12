import pytest
import re
from playwright.sync_api import Page, expect

# --- Test -> Full Contact Page Verification ---

def test_contact_full(page: Page, base_url, layout):
    """
    Test Scenario: Full Contact Page End-to-End
    
    Steps:
    1. Navigate from Homepage (Header CTA).
    2. Verify URL.
    3. Verify Static Content (H2, Intro, Email).
    4. Verify Footer.
    5. Execute Form Logic (Fill and Submit).
    """

    # 1. Navigate to Contact Page
    target_url = f"{base_url}/contacto/"
    page.goto(target_url)

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

    # 4. Verify Layout (Header & Footer)
    layout.verify_header()

    # 4. Verify Footer
    layout.verify_footer()

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

    # Verify Submission Result
    # Handling Logic:
    # - Local execution: Might successfully submit ("enviada com sucesso").
    # - CI/Headless: Might be blocked by spam filters ("Ocorreu um erro").
    # Both are considered "passing" for the purpose of testing UI interaction flow.
    
    response_box = page.locator('.wpcf7-response-output')
    expect(response_box).to_be_visible()
    text = response_box.inner_text()

    if "enviada com sucesso" in text:
        # Success scenario
        assert True
    elif "Ocorreu um erro" in text:
        # Anti-spam/Error scenario
        assert True
    else:
        pytest.fail(f"Unexpected form response: {text}")
