# I import PyTest because it's my main testing framework and manages fixtures.
import pytest

# I import 'os' to access environment variables (like "CI") and make environment decisions.
import os

# I import 'Path' to create and manage file paths (e.g., to robustly create the screenshots folder).
from pathlib import Path  

# I import Playwright's 'expect'. This is what allows me to make verifications (asserts) and wait for elements (which makes tests stable).
from playwright.sync_api import expect


# --- 1. My Custom PyTest Option ---
def pytest_addoption(parser):
    """This function will register my custom '--env' option in PyTest"""
    
    # I use this to add my own flag to the command line.
    parser.addoption(
        "--env",
        action="store",
        default="stag",
        help="The environment my tests should run against (example: 'stag' or 'prod')"
    )


# --- 2. My Base URL Fixture ---
@pytest.fixture(scope="session")
def base_url(request):
    """This fixture will read my '--env' option from the terminal and return the correct URL"""
    
    # I read the environment value the user passed (e.g., "stag")
    env = request.config.getoption("--env")
    
    # I define my URLs in a dictionary
    urls = {
        "stag": "https://stag.palatodigital.com",
        "prod": "https://palatodigital.com"
    }
    
    # I check if the environment is valid. This ensures robustness.
    if env not in urls:
        raise ValueError(f"Environment '{env}' unknown. Valid: {list(urls.keys())}")
    
    # I return the correct URL to the test.
    return urls[env]


# --- 3. Automatic Screenshot Hook on Failure ---
# This hook is called by PyTest after the execution of each test.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    # 1. I get the result of the test execution (passed, failed, skipped)
    outcome = yield
    report = outcome.get_result()

    # 2. I check if the test failed and if it was during the main execution step
    if report.when == "call" and report.failed:
        try:
            # 3. I access the 'page' fixture from the failing test item
            page = item.funcargs["page"]

            # 4. I define the path and filename
            # I ensure the 'screenshots' directory exists (using pathlib for robustness)
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            
            # I create a unique filename using the test name
            screenshot_path = screenshots_dir / f"{item.name}.png"
            
            # 5. I take the screenshot
            # I use the Playwright 'page.screenshot' method directly
            page.screenshot(path=str(screenshot_path))
            
            # I print a message to the terminal for confirmation
            print(f"\n[ 📸 Screenshot ] Saved screenshot to: {screenshot_path}")

        except Exception as e:
            # I handle the error gracefully if the page or browser wasn't available
            print(f"\n[ ❌ Screenshot Error ] Could not take screenshot: {e}")