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


# --- 3. Browser Context Arguments (Viewport) ---
@pytest.fixture(scope="session")
def browser_context_args():
    """
    I override the default browser context arguments to set the viewport size.
    This ensures that the desktop menu is visible and avoids 'hamburger menu' issues.
    """
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


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


# --- 4. Page Layout Fixture (DRY Refactor) ---
class PageLayout:
    """
    Encapsulates common page interactions to avoid code duplication (DRY).
    Includes methods for footer verification, cookie acceptance, and header checks.
    """
    def __init__(self, page):
        self.page = page

    def accept_cookies(self):
        """
        Checks for the cookie banner and accepts it if visible.
        This prevents random timeouts and elements being covered.
        """
        try:
            # "Aceite tudo" button
            cookie_button = self.page.get_by_role("button", name="Aceite tudo")
            if cookie_button.is_visible(timeout=2000):
                cookie_button.click()
                expect(cookie_button).to_be_hidden()
        except Exception:
            # Ignore if not found or already accepted
            pass

    def verify_footer(self):
        """
        Robustly verifies that the footer is visible.
        1. Scrolls to the bottom using JS (handles lazy loading).
        2. Asserts #footer-outer is visible.
        3. Fallback: Checks for 'Palato Digital' text if wrapper has 0 height.
        """
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Primary check: The container
        footer = self.page.locator("#footer-outer")
        
        # We try to assert visibility. 
        # Known issue: On some pages (Privacy/Cookie Policy), #footer-outer has 0 height.
        # We handle this by checking opacity/display or falling back to content check.
        try:
            expect(footer).to_be_visible(timeout=3000)
        except AssertionError:
            # Fallback for 0-height containers: Check for Copyright Text or other common footer elements
            # We try multiple common footer strings to be robust
            try:
                expect(self.page.get_by_text("Palato Digital").last).to_be_visible(timeout=2000)
            except AssertionError:
                 expect(self.page.get_by_text("Todos os direitos reservados", exact=False).first).to_be_visible(timeout=2000)

    def verify_header(self):
        """
        Verifies that the header elements are visible.
        1. Checks for Logo (via ID or Alt Text).
        2. Checks for Menu navigation links.
        """
        # 1. Logo
        # Tries checking by alt text first (accessibility best practice), falls back to ID/Class
        try:
            expect(self.page.get_by_alt_text("Palato Digital").first).to_be_visible()
        except AssertionError:
            expect(self.page.locator("#logo").or_(self.page.locator(".custom-logo-link"))).to_be_visible()

        # 2. Main Navigation Links
        # We check for key pages to ensure the menu is rendered
        nav_pages = ["Serviços", "Sobre", "Vamos falar"]
        for name in nav_pages:
             expect(self.page.get_by_role("link", name=name, exact=False).first).to_be_visible()


@pytest.fixture
def layout(page):
    """
    Returns a PageLayout instance.
    Automatically attempts to accept cookies when instantiated.
    """
    page_layout = PageLayout(page)
    page_layout.accept_cookies()
    return page_layout