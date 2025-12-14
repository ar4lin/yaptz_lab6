"""
Google Search Automation Script
This script demonstrates automated Google search using Selenium WebDriver.
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import config
import screenshot_utils

# Configure logging
logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


def setup_driver():
    """
    Set up and configure Chrome WebDriver with appropriate options.
    
    Returns:
        WebDriver: Configured Chrome WebDriver instance
    """
    options = webdriver.ChromeOptions()
    if config.BROWSER_HEADLESS:
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'--window-size={config.BROWSER_WINDOW_SIZE[0]},{config.BROWSER_WINDOW_SIZE[1]}')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
    
    return driver


def google_search_automation():
    """
    Main function to perform Google search automation.
    
    Returns:
        bool: True if successful, False otherwise
    """
    driver = None
    try:
        logger.info("Starting Google Search automation...")
        
        # Step 1: Setup driver
        driver = setup_driver()
        logger.info("WebDriver initialized successfully")
        
        # Step 2: Open Google
        logger.info(f"Navigating to {config.GOOGLE_URL}")
        driver.get(config.GOOGLE_URL)
        logger.info(f"Current page title: {driver.title}")
        
        # Step 3: Handle cookie consent if present
        try:
            wait = WebDriverWait(driver, 5)
            # Try to find and click "Accept all" or "Reject all" button for cookies
            cookie_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Accept') or contains(., 'Reject')]")
            if cookie_buttons:
                cookie_buttons[0].click()
                logger.info("Cookie consent handled")
        except (TimeoutException, NoSuchElementException):
            logger.info("No cookie consent dialog found or already handled")
        
        # Step 4: Find search box
        logger.info("Locating search box...")
        wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
        
        # Try different selectors for the search box
        search_box = None
        selectors = [
            (By.NAME, "q"),
            (By.CSS_SELECTOR, "textarea[name='q']"),
            (By.CSS_SELECTOR, "input[name='q']"),
            (By.XPATH, "//textarea[@name='q']"),
            (By.XPATH, "//input[@name='q']")
        ]
        
        for by, selector in selectors:
            try:
                search_box = wait.until(EC.presence_of_element_located((by, selector)))
                logger.info(f"Search box found using {by}: {selector}")
                break
            except TimeoutException:
                continue
        
        if not search_box:
            raise Exception("Could not find search box")
        
        # Step 5: Enter search query
        search_query = "Selenium WebDriver Python"
        logger.info(f"Entering search query: {search_query}")
        search_box.clear()
        search_box.send_keys(search_query)
        
        # Step 6: Submit search
        logger.info("Submitting search...")
        search_box.send_keys(Keys.RETURN)
        
        # Step 7: Wait for results to load
        logger.info("Waiting for search results...")
        wait.until(EC.presence_of_element_located((By.ID, "search")))
        logger.info("Search results loaded")
        
        # Step 8: Get first result
        try:
            # Find first search result heading
            first_result = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
            )
            result_text = first_result.text
            logger.info(f"First result title: {result_text}")
            print(f"\n{'='*60}")
            print(f"First Search Result: {result_text}")
            print(f"{'='*60}\n")
        except TimeoutException:
            logger.warning("Could not find first result heading")
        
        # Step 9: Take screenshot of results
        logger.info("Taking screenshot of search results...")
        screenshot_utils.take_screenshot(driver, "google_search_results")
        
        logger.info("Google Search automation completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Error during Google search automation: {str(e)}")
        if driver:
            screenshot_utils.take_screenshot(driver, "google_search_error")
        return False
    
    finally:
        # Step 10: Close browser
        if driver:
            logger.info("Closing browser...")
            driver.quit()


def main():
    """Entry point for the script."""
    print("\n" + "="*60)
    print("Google Search Automation with Selenium WebDriver")
    print("="*60 + "\n")
    
    success = google_search_automation()
    
    if success:
        print("\n✓ Google search automation completed successfully!")
    else:
        print("\n✗ Google search automation failed. Check logs for details.")
    
    return success


if __name__ == "__main__":
    main()
