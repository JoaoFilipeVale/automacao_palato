# I import PyTest. This is the "engine" that will run
# my tests (the 'test_' functions) and validate my 'asserts'.
import pytest

# I also need 'By'. This is my "map", which lets
# me say *how* to find elements (e.g., By.ID, By.LINK_TEXT).
from selenium.webdriver.common.by import By

# I'll need "Explicit Waits".
# This is very important for form tests, where I have
# to wait for the response message to appear (which can be slow).
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# I import the 'Select' class, which is the Selenium
# tool for interacting with <select> tags (dropdowns).
from selenium.webdriver.support.ui import Select


# --- Test -> Check if the contact form works ---

# My test asks for the 'driver' and 'base_url' fixtures (from conftest.py)
def test_contact_form(driver, base_url):

    # 1. The Action: Navigate to the contact page.
    driver.get(base_url + "/contacto/") # (Using the /contacto/ slug we defined)


    # 2. Find the form elements and fill them out.
    driver.find_element(By.NAME, "your-name").send_keys("Automated Test")
    driver.find_element(By.NAME, "your-email").send_keys("test@palatodigital.com")
    driver.find_element(By.NAME, "your-phone").send_keys("932001002")
    
    # 2.1. I need to find the <select> element for the dropdown
    dropdown_element = driver.find_element(By.NAME, "your-interest")

    # 2.1.1 I pass this element to the "Select" tool
    # to gain access to the selection commands.
    select_object = Select(dropdown_element)

    # 2.1.2 I select the option I want,
    # using "select_by_visible_text" (which is the most reliable).
    select_object.select_by_visible_text("Desenvolvimento Web")

    # I continue filling out the rest of the form
    driver.find_element(By.NAME, "your-message").send_keys("This is an automated test message sent by a script.")

    # 2.2. Now I have to find the Privacy Policy checkbox.
    # I need to accept this step to submit the form.
    driver.find_element(By.NAME, "acceptance-policies").click()
    

    # 3. Submit the form
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


    # 4. The Verification (Assert):
    
    # I set up an "Explicit Wait" of 10 seconds.
    wait = WebDriverWait(driver, 10)

    # I tell the "wait" to wait until the element
    # with the class "wpcf7-response-output" (the CF7 response box)
    # is VISIBLE.
    # (I corrected the 'sucess_message_element' typo to 'success_message_element')
    success_message_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "wpcf7-response-output"))
    )

    # Finally, I check if the expected text
    # is inside that element.
    # (This is my test for the reCAPTCHA block)
    # (I corrected the 'except_message' typo to 'expected_message')
    expected_message = "Ocorreu um erro ao tentar enviar a sua mensagem."
    assert expected_message in success_message_element.text