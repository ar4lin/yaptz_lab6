"""
Utility module for creating and managing screenshots.
Provides functions for capturing full page and element screenshots with automatic naming.
"""

import os
from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
import config


def ensure_screenshot_dir():
    """
    Create screenshots directory if it doesn't exist.
    
    Returns:
        str: Path to the screenshots directory
    """
    if not os.path.exists(config.SCREENSHOT_DIR):
        os.makedirs(config.SCREENSHOT_DIR)
        print(f"Created directory: {config.SCREENSHOT_DIR}")
    return config.SCREENSHOT_DIR


def generate_filename(prefix="screenshot", extension=".png"):
    """
    Generate a unique filename with timestamp.
    
    Args:
        prefix (str): Prefix for the filename
        extension (str): File extension (default: .png)
    
    Returns:
        str: Generated filename with timestamp
    """
    timestamp = datetime.now().strftime(config.SCREENSHOT_FORMAT)
    return f"{prefix}_{timestamp}{extension}"


def take_screenshot(driver, name="screenshot"):
    """
    Take a screenshot of the full page and save it with a timestamped name.
    
    Args:
        driver (WebDriver): Selenium WebDriver instance
        name (str): Base name for the screenshot file
    
    Returns:
        str: Full path to the saved screenshot
    """
    ensure_screenshot_dir()
    filename = generate_filename(prefix=name)
    filepath = os.path.join(config.SCREENSHOT_DIR, filename)
    
    try:
        driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Error taking screenshot: {str(e)}")
        return None


def take_element_screenshot(element, name="element"):
    """
    Take a screenshot of a specific element.
    
    Args:
        element (WebElement): Selenium WebElement to capture
        name (str): Base name for the screenshot file
    
    Returns:
        str: Full path to the saved screenshot
    """
    ensure_screenshot_dir()
    filename = generate_filename(prefix=name)
    filepath = os.path.join(config.SCREENSHOT_DIR, filename)
    
    try:
        element.screenshot(filepath)
        print(f"Element screenshot saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Error taking element screenshot: {str(e)}")
        return None


def take_multiple_screenshots(driver, names_list):
    """
    Take multiple screenshots with different names.
    
    Args:
        driver (WebDriver): Selenium WebDriver instance
        names_list (list): List of names for screenshots
    
    Returns:
        list: List of paths to saved screenshots
    """
    screenshots = []
    for name in names_list:
        path = take_screenshot(driver, name)
        if path:
            screenshots.append(path)
    return screenshots
