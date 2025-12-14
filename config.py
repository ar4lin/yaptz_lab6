"""
Configuration file for Selenium WebDriver tests.
Contains timeout values, URLs, and other settings.
"""

import os
import logging
from selenium import webdriver

# Configure logging for this module
logger = logging.getLogger(__name__)

# Browser settings
BROWSER = os.getenv('BROWSER', 'auto')  # 'chrome', 'firefox', 'auto'
HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
BROWSER_WINDOW_SIZE = (1920, 1080)

# Timeout settings (in seconds)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
PAGE_LOAD_TIMEOUT = 30

# URLs for testing
GOOGLE_URL = "https://www.google.com"
SELENIUM_FORM_URL = "https://www.selenium.dev/selenium/web/web-form.html"
NAVIGATION_TEST_URL = "https://www.selenium.dev"

# Screenshot settings
SCREENSHOT_DIR = "screenshots"
SCREENSHOT_FORMAT = "%Y%m%d_%H%M%S"

# Logging settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Legacy compatibility
BROWSER_HEADLESS = HEADLESS


def get_webdriver():
    """
    Creates and returns WebDriver for available browser.
    Tries Chrome, then Firefox, then Chromium.
    Supports headless mode.
    
    Returns:
        WebDriver: Configured WebDriver instance
        
    Raises:
        Exception: If no browser is available
    """
    # Try Chrome first
    if BROWSER == 'auto' or BROWSER == 'chrome':
        try:
            from selenium.webdriver.chrome.service import Service as ChromeService
            
            options = webdriver.ChromeOptions()
            if HEADLESS:
                options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument(f'--window-size={BROWSER_WINDOW_SIZE[0]},{BROWSER_WINDOW_SIZE[1]}')
            
            # Try to use webdriver-manager first, fall back to system driver
            driver_path = None
            try:
                from webdriver_manager.chrome import ChromeDriverManager
                driver_path = ChromeDriverManager().install()
                
                # BUG FIX: Find the correct chromedriver executable
                if os.path.isdir(driver_path):
                    # If path is a directory, look for chromedriver inside
                    driver_path = os.path.join(driver_path, 'chromedriver')
                elif 'THIRD_PARTY_NOTICES' in driver_path or not driver_path.endswith('chromedriver'):
                    # Fix incorrect path from webdriver-manager
                    base_dir = os.path.dirname(driver_path)
                    potential_driver = os.path.join(base_dir, 'chromedriver')
                    if os.path.exists(potential_driver):
                        driver_path = potential_driver
                    else:
                        # Look in parent directory (max 2 levels up)
                        parent_dir = os.path.dirname(base_dir)
                        found = False
                        for root, dirs, files in os.walk(parent_dir):
                            for file in files:
                                if file == 'chromedriver' and os.access(os.path.join(root, file), os.X_OK):
                                    driver_path = os.path.join(root, file)
                                    found = True
                                    break
                            if found:
                                break
            except Exception as wdm_error:
                # Webdriver-manager failed, try system chromedriver
                logger.warning(f"Webdriver-manager failed: {wdm_error}")
                driver_path = None
            
            # Create service with driver path (None means use system PATH)
            if driver_path and os.path.exists(driver_path):
                service = ChromeService(executable_path=driver_path)
            else:
                # Use system chromedriver from PATH
                service = ChromeService()
            
            driver = webdriver.Chrome(service=service, options=options)
            driver.implicitly_wait(IMPLICIT_WAIT)
            driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
            return driver
            
        except Exception as e:
            if BROWSER == 'chrome':
                # User explicitly requested Chrome, so fail
                raise Exception(f"Chrome unavailable: {e}") from e
            logger.info(f"Chrome unavailable: {e}")
    
    # Try Firefox second
    if BROWSER == 'auto' or BROWSER == 'firefox':
        try:
            from selenium.webdriver.firefox.service import Service as FirefoxService
            
            options = webdriver.FirefoxOptions()
            if HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument(f'--width={BROWSER_WINDOW_SIZE[0]}')
            options.add_argument(f'--height={BROWSER_WINDOW_SIZE[1]}')
            
            # Try to use webdriver-manager first, fall back to system driver
            driver_path = None
            try:
                from webdriver_manager.firefox import GeckoDriverManager
                driver_path = GeckoDriverManager().install()
            except Exception as wdm_error:
                # Webdriver-manager failed, try system geckodriver
                logger.warning(f"Webdriver-manager failed: {wdm_error}")
                driver_path = None
            
            # Create service with driver path (None means use system PATH)
            if driver_path and os.path.exists(driver_path):
                service = FirefoxService(executable_path=driver_path)
            else:
                # Use system geckodriver from PATH
                service = FirefoxService()
            
            driver = webdriver.Firefox(service=service, options=options)
            driver.implicitly_wait(IMPLICIT_WAIT)
            driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
            return driver
            
        except Exception as e:
            if BROWSER == 'firefox':
                # User explicitly requested Firefox, so fail
                raise Exception(f"Firefox unavailable: {e}") from e
            logger.info(f"Firefox unavailable: {e}")
    
    # No browser available
    raise Exception("Unable to find an available browser! Please install Chrome or Firefox.")
