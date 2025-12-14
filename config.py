"""
Configuration file for Selenium WebDriver tests.
Contains timeout values, URLs, and other settings.
"""

# Timeout settings (in seconds)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30

# URLs for testing
GOOGLE_URL = "https://www.google.com"
SELENIUM_FORM_URL = "https://www.selenium.dev/selenium/web/web-form.html"
NAVIGATION_TEST_URL = "https://www.selenium.dev"

# Screenshot settings
SCREENSHOT_DIR = "screenshots"
SCREENSHOT_FORMAT = "%Y%m%d_%H%M%S"

# Browser settings
BROWSER_HEADLESS = False  # Set to True for headless mode
BROWSER_WINDOW_SIZE = (1920, 1080)

# Logging settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
