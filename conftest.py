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


# --- Add my '--env' option to PyTest ---

# This is a special PyTest "hook" function. PyTest will
# find it and run it automatically when I start the tests.
# The "parser" is the object that will allow me to "add new options"
# to my command line.
def pytest_addoption(parser):
    """This function will register my custom '--env' option in PyTest"""

    # Here I'll add my own command-line flag.
    parser.addoption(
        # The name of my flag (example: --env=prod)
        "--env",

        # The action: "store" means "save the value that comes next"
        # (example: --env="prod" -> I want it to store "prod").
        action="store",

        # The default value: If I just run "pytest" without
        # the '--env' flag, I want the value "stag" to be used by default.
        default="stag",

        # The help message that will appear if I run "pytest --help"
        help="The environment my tests should run against (example: 'stag' or 'prod')"
    )


# --- Create my "base_url" fixture ---

# The "@pytest.fixture" is a "decorator". I'll use it to turn
# this function into a "helper" that can "provide" the URL
# to any test that asks for it.
@pytest.fixture
def base_url(request: pytest.FixtureRequest):
    """This fixture will read my '--env' option from the terminal and return the correct URL"""

    # "request" is a special PyTest argument
    # It will give me access to the "context" of the test, including the
    # command-line options that I just defined.
    
    # 1. I'll read the value I passed (example: "stag" or "prod")
    env = request.config.getoption("--env")

    # 2. I'll define my URLs in a dictionary (it's cleaner)
    urls = {
        "stag": "https://stag.palatodigital.com", # Development URL
        "prod": "https://palatodigital.com" # Production URL
    }

    # 3. Error Handling:
    # I'll check if the 'env' I typed exists in my URLs.
    # This is important to "fail fast" if I make a mistake
    # (example: --env=production)
    if env not in urls:
        raise pytest.UsageError(f"Environment '{env}' unknown. Valid: {list(urls.keys())}")
    
    # 4. Return the correct URL.
    # Any test I write that asks for 'base_url' as an argument
    # (example: def test_foo(base_url): ...)
    # will receive the URL that this line returns.
    return urls[env]


# --- Create my "driver" fixture ---

# The '@pytest.fixture' turns this function into a global "helper" for all tests.
@pytest.fixture
def driver():
    """This fixture will open and close the browser for my tests"""

    # 1. I'll configure ChromeDriver automatically.
    # I'll use ChromeDriverManager().install() so it downloads
    # the correct driver for my version of Chrome.
    s = Service(ChromeDriverManager().install())

    # 2. Now, I'll start the Chrome browser,
    # telling it to use the "Service" I just configured.
    driver = webdriver.Chrome(service=s)

    # 3. My site (Wordpress) can be slow to load elements.
    # To make my tests more stable, I'll add an
    # implicit wait of 5 seconds.
    driver.implicitly_wait(5)

    # 4. This is the central part of the fixture: the 'yield'.
    # I "hand over" the 'driver' (the browser) to the test that asked for it.
    yield driver

    # 5. After the test finishes, I'll return here.
    # This part of the code will close the browser,
    # ensuring no windows are left open after the tests.
    driver.quit()