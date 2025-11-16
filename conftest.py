# I import 'os' (Operating System) so I can read
# "Environment Variables" and detect if I'm on GitHub.
import os

# I import PyTest for my "hook" and "fixture" functions.
import pytest

# I import the Selenium tools (webdriver, Service)
# and the manager (ChromeDriverManager) here.
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


# ---  MY "driver" FIXTURE ---
@pytest.fixture
def driver():
    """This fixture will open and close the browser for my tests"""

    # 1. I'll configure the OPTIONS for Chrome first.
    # These options are needed for BOTH my PC and GitHub.
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 2.  --- THIS IS THE "SMART" CHECK ---
    # I'll check if I'm running inside a GitHub Action (CI = Continuous Integration)
    # The 'os.getenv("CI")' will return "true" if I'm on GitHub,
    # and "None" if I'm on my local PC.
    if os.getenv("CI") == "true":
        # If I'm on GitHub:
        # The 'setup-chrome' action in my main.yml already installed
        # the correct chromedriver. I'll just pass the options.
        driver = webdriver.Chrome(options=options)
    else:
        # If I'm on my LOCAL PC:
        # I need the full 'Service' and 'WebDriverManager'
        # to download the driver for me.
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=options)

    # 3. I'll add an implicit wait.
    driver.implicitly_wait(5)

    # 4. I "hand over" the 'driver' to the test.
    yield driver

    # 5. After the test, I close the browser.
    driver.quit()