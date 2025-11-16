# I import PyTest. I need this so that
# PyTest recognizes my special functions,
# like "pytest_addoption" and '@pytest.fixture'.
import pytest

# I import the Selenium tools (webdriver, Service)
# and the manager (ChromeDriverManager) here,
# because my 'driver' fixture (which opens the browser) will use this.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# I need to import 'Options' to tell Chrome
# HOW it should run (e.g., "headless").
from selenium.webdriver.chrome.options import Options


# --- Add my '--env' option to PyTest ---

# (This part stays exactly the same)
def pytest_addoption(parser):
    """This function will register my custom '--env' option in PyTest"""
    parser.addoption(
        "--env",
        action="store",
        default="stag",
        help="The environment my tests should run against (example: 'stag' or 'prod')"
    )


# --- Create my "base_url" fixture ---

# (This part also stays exactly the same)
@pytest.fixture
def base_url(request: pytest.FixtureRequest):
    """This fixture will read my '--env' option from the terminal and return the correct URL"""
    
    # 1. I'll read the value I passed
    env = request.config.getoption("--env")

    # 2. I'll define my URLs
    urls = {
        "stag": "https://stag.palatodigital.com", # <-- Development URL
        "prod": "https://palatodigital.com" # <-- Production URL
    }

    # 3. Error Handling
    if env not in urls:
        raise pytest.UsageError(f"Environment '{env}' unknown. Valid: {list(urls.keys())}")
    
    # 4. Return the correct URL
    return urls[env]


# --- MY "driver" FIXTURE ---

@pytest.fixture
def driver():
    """This fixture will open and close the browser for my tests"""

    # 1. I'll configure the OPTIONS for Chrome first.
    options = Options()
    options.add_argument("--headless")          # <-- This is the magic line that runs Chrome without a window.
    options.add_argument("--no-sandbox")        # <-- This is required to run as "root" in the Linux container.
    options.add_argument("--disable-dev-shm-usage") # <-- This avoids memory issues in the VM.
    
    # 2. I'll configure ChromeDriver automatically.
    s = Service(ChromeDriverManager().install())

    # 3. Now, I'll start the Chrome browser,
    # PASSING MY NEW 'options' to it.
    driver = webdriver.Chrome(service=s, options=options)

    # 4. I'll add an implicit wait.
    driver.implicitly_wait(5)

    # 5. I "hand over" the 'driver' to the test.
    yield driver

    # 6. After the test, I close the browser.
    driver.quit()