import pytest
from playwright.sync_api import Page, expect

# --- Test -> Check if the contact form works ---

# I ask for 'page' (Playwright) and 'base_url' (my custom fixture).
def test_contact_form(page: Page, base_url):

    # 1. The Action: Navigate to contact page
    # I use Python's f-string to build the full URL cleanly.
    page.goto(f"{base_url}/contacto/") 

    # 2. Fill the form
    # Playwright uses the locator('[name="..."]') to find elements
    # and automatically waits for them to be editable.
    
    page.locator('[name="your-name"]').fill("Automated Test Playwright")
    page.locator('[name="your-email"]').fill("test@palatodigital.com")
    page.locator('[name="your-phone"]').fill("932001002")

    # 2.1. Dropdown is now simple:
    # I find the element and select the option by its visible text.
    page.locator('[name="your-interest"]').select_option(label="Desenvolvimento Web")

    # I continue filling out the rest of the form
    page.locator('[name="your-message"]').fill("This is an automated test message sent by a script.")

    # 2.2. Checkbox: I use the robust '.check()' command.
    page.locator('[name="acceptance-policies"]').check()

    # 3. Submit
    page.locator('input[type="submit"]').click()

    # 4. The Verification (Assert):
    # The 'expect' function automatically waits up to 30s for the
    # text to appear.
    
    expected_error_message = "Ocorreu um erro ao tentar enviar a sua mensagem. Por favor, tente novamente mais tarde."
    
    # I define the locator for the response box.
    response_box = page.locator('.wpcf7-response-output')
    
    # I check if the response box contains the specific error text.
    expect(response_box).to_contain_text(expected_error_message)