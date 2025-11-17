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

    # I'll define the text I'm waiting for
    # (It doesn't need to be the full sentence, just a unique part!)
    expected_error = "Ocorreu um erro ao tentar enviar a sua mensagem. Por favor, tente novamente mais tarde." 

    # I tell the 'wait' to wait UP TO 10 seconds
    # for the text "Ocorreu um erro" to be present
    # INSIDE the element with the class 'wpcf7-response-output'.
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "wpcf7-response-output"), # 1. Where (The locator)
            expected_error                            # 2. What (The text)
        )
    )

    # 5. The Final Assert
    # If the 'wait.until' passed, it means the text appeared!
    # The test is 99% won. We can now do a final 'assert'
    # just to confirm the full text is there.
    final_text = driver.find_element(By.CLASS_NAME, "wpcf7-response-output").text
    full_expected_message = "Ocorreu um erro ao tentar enviar a sua mensagem. Por favor, tente novamente mais tarde."

    # I "assert" that the complete error message is in the final text.
    assert full_expected_message in final_text