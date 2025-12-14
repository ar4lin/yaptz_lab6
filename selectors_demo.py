"""
Selectors Demonstration Script
Demonstrates different types of selectors: XPath and CSS selectors.
"""

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def demonstrate_css_selectors(driver):
    """
    Demonstrate different CSS selector techniques.
    
    Args:
        driver: WebDriver instance
    """
    print("\n" + "="*60)
    print("CSS Selectors Demonstration")
    print("="*60)
    
    # CSS by ID
    logger.info("Finding element by ID using CSS selector...")
    try:
        element = driver.find_element(By.CSS_SELECTOR, "#my-text-id")
        print(f"✓ CSS by ID (#my-text-id): Found element with tag '{element.tag_name}'")
        logger.info("Element found by CSS ID selector")
    except Exception as e:
        logger.warning(f"Could not find element by CSS ID: {str(e)}")
    
    # CSS by class
    logger.info("Finding elements by class using CSS selector...")
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, ".form-label")
        print(f"✓ CSS by class (.form-label): Found {len(elements)} elements")
        logger.info(f"Found {len(elements)} elements by CSS class selector")
    except Exception as e:
        logger.warning(f"Could not find elements by CSS class: {str(e)}")
    
    # CSS by attribute
    logger.info("Finding element by attribute using CSS selector...")
    try:
        element = driver.find_element(By.CSS_SELECTOR, "input[name='my-password']")
        print(f"✓ CSS by attribute (input[name='my-password']): Found element")
        logger.info("Element found by CSS attribute selector")
    except Exception as e:
        logger.warning(f"Could not find element by CSS attribute: {str(e)}")
    
    # CSS by type
    logger.info("Finding elements by type using CSS selector...")
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
        print(f"✓ CSS by type (button[type='submit']): Found {len(elements)} elements")
        logger.info(f"Found {len(elements)} elements by CSS type selector")
    except Exception as e:
        logger.warning(f"Could not find elements by CSS type: {str(e)}")
    
    # CSS descendant combinator
    logger.info("Finding elements using CSS descendant combinator...")
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "form input")
        print(f"✓ CSS descendant (form input): Found {len(elements)} elements")
        logger.info(f"Found {len(elements)} elements using CSS descendant combinator")
    except Exception as e:
        logger.warning(f"Could not find elements using CSS descendant: {str(e)}")
    
    # CSS child combinator
    logger.info("Finding elements using CSS child combinator...")
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "form > div")
        print(f"✓ CSS child (form > div): Found {len(elements)} elements")
        logger.info(f"Found {len(elements)} elements using CSS child combinator")
    except Exception as e:
        logger.warning(f"Could not find elements using CSS child: {str(e)}")
    
    # CSS pseudo-class
    logger.info("Finding elements using CSS pseudo-class...")
    try:
        element = driver.find_element(By.CSS_SELECTOR, "input:first-of-type")
        print(f"✓ CSS pseudo-class (input:first-of-type): Found element")
        logger.info("Element found using CSS pseudo-class selector")
    except Exception as e:
        logger.warning(f"Could not find element using CSS pseudo-class: {str(e)}")


def demonstrate_xpath_selectors(driver):
    """
    Demonstrate different XPath selector techniques.
    
    Args:
        driver: WebDriver instance
    """
    print("\n" + "="*60)
    print("XPath Selectors Demonstration")
    print("="*60)
    
    # XPath absolute path (not recommended but shown for demonstration)
    logger.info("Finding element using absolute XPath...")
    try:
        element = driver.find_element(By.XPATH, "/html/body/main/div/form")
        print(f"✓ XPath absolute (/html/body/main/div/form): Found element with tag '{element.tag_name}'")
        logger.info("Element found using absolute XPath")
    except Exception as e:
        logger.warning(f"Could not find element using absolute XPath: {str(e)}")
    
    # XPath by ID
    logger.info("Finding element by ID using XPath...")
    try:
        element = driver.find_element(By.XPATH, "//*[@id='my-text-id']")
        print(f"✓ XPath by ID (//*[@id='my-text-id']): Found element")
        logger.info("Element found by XPath ID selector")
    except Exception as e:
        logger.warning(f"Could not find element by XPath ID: {str(e)}")
    
    # XPath by attribute
    logger.info("Finding element by attribute using XPath...")
    try:
        element = driver.find_element(By.XPATH, "//input[@name='my-password']")
        print(f"✓ XPath by attribute (//input[@name='my-password']): Found element")
        logger.info("Element found by XPath attribute selector")
    except Exception as e:
        logger.warning(f"Could not find element by XPath attribute: {str(e)}")
    
    # XPath by text content
    logger.info("Finding element by text using XPath...")
    try:
        element = driver.find_element(By.XPATH, "//button[text()='Submit']")
        print(f"✓ XPath by text (//button[text()='Submit']): Found element")
        logger.info("Element found by XPath text selector")
    except Exception as e:
        logger.warning(f"Could not find element by XPath text: {str(e)}")
    
    # XPath contains
    logger.info("Finding elements using XPath contains...")
    try:
        elements = driver.find_elements(By.XPATH, "//label[contains(@class, 'form-label')]")
        print(f"✓ XPath contains (//label[contains(@class, 'form-label')]): Found {len(elements)} elements")
        logger.info(f"Found {len(elements)} elements using XPath contains")
    except Exception as e:
        logger.warning(f"Could not find elements using XPath contains: {str(e)}")
    
    # XPath starts-with
    logger.info("Finding elements using XPath starts-with...")
    try:
        elements = driver.find_elements(By.XPATH, "//input[starts-with(@name, 'my-')]")
        print(f"✓ XPath starts-with (//input[starts-with(@name, 'my-')]): Found {len(elements)} elements")
        logger.info(f"Found {len(elements)} elements using XPath starts-with")
    except Exception as e:
        logger.warning(f"Could not find elements using XPath starts-with: {str(e)}")
    
    # XPath following-sibling
    logger.info("Finding elements using XPath following-sibling...")
    try:
        element = driver.find_element(By.XPATH, "//label[@for='my-text-id']/following-sibling::input")
        print(f"✓ XPath following-sibling: Found element")
        logger.info("Element found using XPath following-sibling")
    except Exception as e:
        logger.warning(f"Could not find element using XPath following-sibling: {str(e)}")
    
    # XPath parent
    logger.info("Finding element using XPath parent axis...")
    try:
        element = driver.find_element(By.XPATH, "//input[@id='my-text-id']/parent::div")
        print(f"✓ XPath parent: Found parent element")
        logger.info("Element found using XPath parent axis")
    except Exception as e:
        logger.warning(f"Could not find element using XPath parent: {str(e)}")
    
    # XPath with index
    logger.info("Finding element using XPath with index...")
    try:
        element = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        print(f"✓ XPath with index ((//input[@type='text'])[1]): Found first text input")
        logger.info("Element found using XPath with index")
    except Exception as e:
        logger.warning(f"Could not find element using XPath with index: {str(e)}")


def compare_selector_performance(driver):
    """
    Compare performance of different selector types.
    
    Args:
        driver: WebDriver instance
    """
    print("\n" + "="*60)
    print("Selector Performance Comparison")
    print("="*60)
    
    # Test CSS ID selector performance
    start_time = time.time()
    try:
        for _ in range(10):
            driver.find_element(By.CSS_SELECTOR, "#my-text-id")
        css_id_time = (time.time() - start_time) * 1000
        print(f"CSS ID selector (10 iterations): {css_id_time:.2f}ms")
    except Exception as e:
        logger.warning(f"CSS ID selector failed: {str(e)}")
    
    # Test XPath ID selector performance
    start_time = time.time()
    try:
        for _ in range(10):
            driver.find_element(By.XPATH, "//*[@id='my-text-id']")
        xpath_id_time = (time.time() - start_time) * 1000
        print(f"XPath ID selector (10 iterations): {xpath_id_time:.2f}ms")
    except Exception as e:
        logger.warning(f"XPath ID selector failed: {str(e)}")
    
    # Test CSS class selector performance
    start_time = time.time()
    try:
        for _ in range(10):
            driver.find_elements(By.CSS_SELECTOR, ".form-label")
        css_class_time = (time.time() - start_time) * 1000
        print(f"CSS class selector (10 iterations): {css_class_time:.2f}ms")
    except Exception as e:
        logger.warning(f"CSS class selector failed: {str(e)}")
    
    # Test XPath class selector performance
    start_time = time.time()
    try:
        for _ in range(10):
            driver.find_elements(By.XPATH, "//label[contains(@class, 'form-label')]")
        xpath_class_time = (time.time() - start_time) * 1000
        print(f"XPath class selector (10 iterations): {xpath_class_time:.2f}ms")
    except Exception as e:
        logger.warning(f"XPath class selector failed: {str(e)}")
    
    print("\nNote: CSS selectors are generally faster and more readable.")
    print("XPath is more powerful for complex hierarchies and text matching.")


def selectors_demo():
    """
    Main function to demonstrate different selector types.
    
    Returns:
        bool: True if successful, False otherwise
    """
    driver = None
    try:
        logger.info("Starting Selectors Demonstration...")
        
        # Setup driver
        driver = setup_driver()
        logger.info("WebDriver initialized successfully")
        
        # Navigate to test page
        logger.info(f"Navigating to {config.SELENIUM_FORM_URL}")
        driver.get(config.SELENIUM_FORM_URL)
        logger.info(f"Current page title: {driver.title}")
        
        # Take initial screenshot
        screenshot_utils.take_screenshot(driver, "selectors_demo_page")
        
        # Demonstrate CSS selectors
        demonstrate_css_selectors(driver)
        
        # Demonstrate XPath selectors
        demonstrate_xpath_selectors(driver)
        
        # Compare performance
        compare_selector_performance(driver)
        
        logger.info("Selectors demonstration completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Error during selectors demonstration: {str(e)}")
        if driver:
            screenshot_utils.take_screenshot(driver, "selectors_demo_error")
        return False
    
    finally:
        if driver:
            logger.info("Closing browser...")
            driver.quit()


def main():
    """Entry point for the script."""
    print("\n" + "="*60)
    print("XPath and CSS Selectors Demonstration")
    print("="*60 + "\n")
    
    success = selectors_demo()
    
    if success:
        print("\n✓ Selectors demonstration completed successfully!")
    else:
        print("\n✗ Selectors demonstration failed. Check logs for details.")
    
    return success


if __name__ == "__main__":
    main()
