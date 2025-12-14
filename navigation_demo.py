"""
Navigation Demonstration Script
Demonstrates browser navigation operations: back, forward, refresh, windows, and tabs.
"""

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import screenshot_utils

# Configure logging
logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


def demonstrate_basic_navigation(driver):
    """
    Demonstrate basic navigation operations: back, forward, refresh.
    
    Args:
        driver: WebDriver instance
    """
    print("\n" + "="*60)
    print("Basic Navigation Demonstration")
    print("="*60)
    
    # Navigate to first page
    logger.info(f"Navigating to {config.NAVIGATION_TEST_URL}")
    driver.get(config.NAVIGATION_TEST_URL)
    first_url = driver.current_url
    print(f"✓ First page loaded: {first_url}")
    print(f"  Title: {driver.title}")
    screenshot_utils.take_screenshot(driver, "navigation_page1")
    time.sleep(1)
    
    # Find and click on a link
    try:
        wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
        # Try to find a link to navigate to
        links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
        if links:
            # Filter for internal links - cache href to avoid repeated DOM queries
            internal_links = []
            for link in links:
                href = link.get_attribute("href")
                if href and config.NAVIGATION_TEST_URL in href and href != first_url:
                    internal_links.append(link)
            
            if internal_links:
                link = internal_links[0]
                link_text = link.text[:50] if link.text else "Link"
                link_url = link.get_attribute("href")
                logger.info(f"Clicking link: {link_text} -> {link_url}")
                link.click()
                time.sleep(2)
                
                second_url = driver.current_url
                print(f"✓ Navigated to second page: {second_url}")
                print(f"  Title: {driver.title}")
                screenshot_utils.take_screenshot(driver, "navigation_page2")
            else:
                # If no suitable internal link, navigate to a known page
                logger.info("No suitable link found, navigating to documentation")
                driver.get(f"{config.NAVIGATION_TEST_URL}/documentation")
                time.sleep(2)
                print(f"✓ Navigated to: {driver.current_url}")
                screenshot_utils.take_screenshot(driver, "navigation_page2")
    except Exception as e:
        logger.warning(f"Could not click link: {str(e)}")
        # Navigate manually to another page
        driver.get(f"{config.NAVIGATION_TEST_URL}/documentation")
        time.sleep(1)
        print(f"✓ Navigated manually to: {driver.current_url}")
    
    # Demonstrate back navigation
    logger.info("Testing back() navigation...")
    driver.back()
    time.sleep(1)
    print(f"✓ Navigated back to: {driver.current_url}")
    print(f"  Title: {driver.title}")
    screenshot_utils.take_screenshot(driver, "navigation_back")
    
    # Demonstrate forward navigation
    logger.info("Testing forward() navigation...")
    driver.forward()
    time.sleep(1)
    print(f"✓ Navigated forward to: {driver.current_url}")
    print(f"  Title: {driver.title}")
    screenshot_utils.take_screenshot(driver, "navigation_forward")
    
    # Demonstrate refresh
    logger.info("Testing refresh() navigation...")
    driver.refresh()
    time.sleep(1)
    print(f"✓ Page refreshed: {driver.current_url}")
    print(f"  Title: {driver.title}")
    screenshot_utils.take_screenshot(driver, "navigation_refresh")


def demonstrate_window_management(driver):
    """
    Demonstrate window and tab management.
    
    Args:
        driver: WebDriver instance
    """
    print("\n" + "="*60)
    print("Window and Tab Management Demonstration")
    print("="*60)
    
    # Get current window handle
    original_window = driver.current_window_handle
    logger.info(f"Original window handle: {original_window}")
    print(f"✓ Original window: {driver.current_url}")
    
    # Get all window handles before opening new tab
    original_windows = driver.window_handles
    print(f"  Number of windows: {len(original_windows)}")
    
    # Open a new tab
    logger.info("Opening new tab...")
    driver.switch_to.new_window('tab')
    time.sleep(1)
    
    # Get all window handles after opening new tab
    new_windows = driver.window_handles
    print(f"✓ New tab opened")
    print(f"  Number of windows: {len(new_windows)}")
    
    # Navigate in the new tab
    new_url = f"{config.NAVIGATION_TEST_URL}/downloads"
    logger.info(f"Navigating in new tab to: {new_url}")
    driver.get(new_url)
    time.sleep(1)
    print(f"✓ New tab content: {driver.current_url}")
    print(f"  Title: {driver.title}")
    screenshot_utils.take_screenshot(driver, "navigation_new_tab")
    
    # Switch back to original window
    logger.info("Switching back to original window...")
    driver.switch_to.window(original_window)
    time.sleep(1)
    print(f"✓ Switched back to original window: {driver.current_url}")
    print(f"  Title: {driver.title}")
    screenshot_utils.take_screenshot(driver, "navigation_original_window")
    
    # Switch to new tab again
    logger.info("Switching to new tab...")
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    time.sleep(1)
    print(f"✓ Switched to new tab: {driver.current_url}")
    
    # Close the new tab
    logger.info("Closing new tab...")
    driver.close()
    time.sleep(1)
    print(f"✓ New tab closed")
    
    # Switch back to original window
    driver.switch_to.window(original_window)
    print(f"✓ Back to original window: {driver.current_url}")
    print(f"  Number of windows: {len(driver.window_handles)}")
    
    # Try opening a new window (not tab)
    logger.info("Opening new window...")
    driver.switch_to.new_window('window')
    time.sleep(1)
    print(f"✓ New window opened")
    print(f"  Number of windows: {len(driver.window_handles)}")
    
    # Navigate in the new window
    new_url = f"{config.NAVIGATION_TEST_URL}/about"
    logger.info(f"Navigating in new window to: {new_url}")
    driver.get(new_url)
    time.sleep(1)
    print(f"✓ New window content: {driver.current_url}")
    screenshot_utils.take_screenshot(driver, "navigation_new_window")
    
    # Close new window and switch back
    logger.info("Closing new window...")
    driver.close()
    driver.switch_to.window(original_window)
    time.sleep(1)
    print(f"✓ New window closed, back to original")
    print(f"  Number of windows: {len(driver.window_handles)}")


def demonstrate_url_navigation(driver):
    """
    Demonstrate direct URL navigation with get().
    
    Args:
        driver: WebDriver instance
    """
    print("\n" + "="*60)
    print("Direct URL Navigation Demonstration")
    print("="*60)
    
    urls = [
        config.NAVIGATION_TEST_URL,
        f"{config.NAVIGATION_TEST_URL}/documentation",
        f"{config.NAVIGATION_TEST_URL}/projects",
    ]
    
    for i, url in enumerate(urls, 1):
        logger.info(f"Navigating to URL {i}: {url}")
        try:
            driver.get(url)
            time.sleep(1)
            print(f"✓ Navigation {i}: {driver.current_url}")
            print(f"  Title: {driver.title}")
            logger.info(f"Successfully navigated to: {url}")
        except Exception as e:
            logger.warning(f"Could not navigate to {url}: {str(e)}")
            print(f"✗ Navigation {i} failed: {url}")


def navigation_demo():
    """
    Main function to demonstrate navigation operations.
    
    Returns:
        bool: True if successful, False otherwise
    """
    driver = None
    try:
        logger.info("Starting Navigation Demonstration...")
        
        # Setup driver
        driver = config.get_webdriver()
        logger.info("WebDriver initialized successfully")
        
        # Demonstrate basic navigation
        demonstrate_basic_navigation(driver)
        
        # Demonstrate window management
        demonstrate_window_management(driver)
        
        # Demonstrate URL navigation
        demonstrate_url_navigation(driver)
        
        logger.info("Navigation demonstration completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Error during navigation demonstration: {str(e)}")
        if driver:
            screenshot_utils.take_screenshot(driver, "navigation_demo_error")
        return False
    
    finally:
        if driver:
            logger.info("Closing browser...")
            driver.quit()


def main():
    """Entry point for the script."""
    print("\n" + "="*60)
    print("Browser Navigation Demonstration")
    print("="*60 + "\n")
    
    success = navigation_demo()
    
    if success:
        print("\n✓ Navigation demonstration completed successfully!")
    else:
        print("\n✗ Navigation demonstration failed. Check logs for details.")
    
    return success


if __name__ == "__main__":
    main()
