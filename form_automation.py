"""
Form Automation Script
Demonstrates automated form filling using Selenium WebDriver.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
import config
import screenshot_utils

# Configure logging
logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


def form_automation():
    """
    Main function to perform form automation.
    
    Returns:
        bool: True if successful, False otherwise
    """
    driver = None
    try:
        logger.info("Starting Form Automation...")
        
        # Step 1: Setup driver
        driver = config.get_webdriver()
        logger.info("WebDriver initialized successfully")
        
        # Step 2: Navigate to form
        logger.info(f"Navigating to {config.SELENIUM_FORM_URL}")
        driver.get(config.SELENIUM_FORM_URL)
        logger.info(f"Current page title: {driver.title}")
        
        # Step 3: Take screenshot before filling
        logger.info("Taking screenshot before filling form...")
        screenshot_utils.take_screenshot(driver, "form_before_fill")
        
        wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
        
        # Step 4: Fill text input
        logger.info("Filling text input field...")
        text_input = wait.until(EC.presence_of_element_located((By.ID, "my-text-id")))
        text_input.clear()
        text_input.send_keys("Selenium WebDriver Test")
        logger.info("Text input filled")
        
        # Step 5: Fill password field
        logger.info("Filling password field...")
        password_input = driver.find_element(By.NAME, "my-password")
        password_input.clear()
        password_input.send_keys("SecurePassword123!")
        logger.info("Password field filled")
        
        # Step 6: Fill textarea
        logger.info("Filling textarea...")
        textarea = driver.find_element(By.NAME, "my-textarea")
        textarea.clear()
        textarea.send_keys("This is a test message.\nMultiple lines are supported.\nThank you!")
        logger.info("Textarea filled")
        
        # Step 7: Select from dropdown
        logger.info("Selecting from dropdown...")
        dropdown = Select(driver.find_element(By.NAME, "my-select"))
        dropdown.select_by_value("2")  # Select second option
        logger.info("Dropdown option selected")
        
        # Step 8: Select checkboxes
        logger.info("Selecting checkboxes...")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        for i, checkbox in enumerate(checkboxes[:2]):  # Select first two checkboxes
            if not checkbox.is_selected():
                checkbox.click()
                logger.info(f"Checkbox {i+1} selected")
        
        # Step 9: Select radio button
        logger.info("Selecting radio button...")
        radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
        if radio_buttons:
            if not radio_buttons[0].is_selected():
                radio_buttons[0].click()
                logger.info("Radio button selected")
        
        # Step 10: Fill date picker
        logger.info("Filling date picker...")
        try:
            datepicker = driver.find_element(By.NAME, "my-datepicker")
            datepicker.send_keys("01/01/2024")
            logger.info("Date picker filled")
        except Exception as e:
            logger.warning(f"Could not fill date picker: {str(e)}")
        
        # Step 11: Fill color picker
        logger.info("Selecting color...")
        try:
            color_picker = driver.find_element(By.NAME, "my-colors")
            driver.execute_script("arguments[0].value = '#FF5733';", color_picker)
            logger.info("Color selected")
        except Exception as e:
            logger.warning(f"Could not select color: {str(e)}")
        
        # Step 12: Take screenshot after filling
        logger.info("Taking screenshot after filling form...")
        screenshot_utils.take_screenshot(driver, "form_after_fill")
        
        # Step 13: Submit form
        logger.info("Submitting form...")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Step 14: Wait for submission and verify
        logger.info("Waiting for form submission...")
        try:
            # Wait for URL change or success message
            wait.until(lambda d: "Received!" in d.page_source or d.current_url != config.SELENIUM_FORM_URL)
            logger.info(f"Form submitted successfully! Current URL: {driver.current_url}")
            
            # Take screenshot after submission
            screenshot_utils.take_screenshot(driver, "form_after_submit")
            
            # Check for success message
            if "Received!" in driver.page_source:
                logger.info("Success message found on page")
                print(f"\n{'='*60}")
                print("Form submitted successfully!")
                print("Success message: 'Received!' found on page")
                print(f"{'='*60}\n")
            
        except TimeoutException:
            logger.warning("Could not verify form submission")
        
        logger.info("Form automation completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Error during form automation: {str(e)}")
        if driver:
            screenshot_utils.take_screenshot(driver, "form_automation_error")
        return False
    
    finally:
        # Step 15: Close browser
        if driver:
            logger.info("Closing browser...")
            driver.quit()


def main():
    """Entry point for the script."""
    print("\n" + "="*60)
    print("Form Automation with Selenium WebDriver")
    print("="*60 + "\n")
    
    success = form_automation()
    
    if success:
        print("\n✓ Form automation completed successfully!")
    else:
        print("\n✗ Form automation failed. Check logs for details.")
    
    return success


if __name__ == "__main__":
    main()
