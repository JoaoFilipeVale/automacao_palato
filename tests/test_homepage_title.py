# I import PyTest. This is the "engine" that will run
# my tests (the 'test_' functions) and validate my 'asserts'.
import pytest


# --- Test -> Verify the website's main page title ---

# My test asks for "driver" and "base_url".
# PyTest will fetch BOTH fixtures from the "conftest.py" file.
def test_homepage_title(driver, base_url):
    
    # 1. The Action: Open the URL that 'base_url' gave me
    driver.get(base_url)

    # 2. The Verification (Assert):
    
    # I define the exact title I expect the page to have.
    # (I copied this directly from my site's <title> tag).
    expected_title = "Palato Digital – O sabor da inovação digital"

    # The 'assert' is the heart of the test.
    # I "assert" that the actual title (driver.title) MUST BE EQUAL
    # to my expected title.
    assert driver.title == expected_title