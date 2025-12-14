"""
Main Script - Selenium WebDriver Lab 6
Runs all automation tests sequentially with error handling and reporting.
"""

import logging
import sys
from datetime import datetime
import config
import screenshot_utils

# Import all test modules
import google_search
import form_automation
import selectors_demo
import navigation_demo


def check_browser_availability():
    """
    Checks browser availability before running tests.
    
    Returns:
        bool: True if browser is available, False otherwise
    """
    print("\n" + "="*80)
    print("Checking browser availability...")
    print("="*80)
    
    try:
        driver = config.get_webdriver()
        driver.quit()
        print("✓ Browser successfully initialized!")
        return True
    except Exception as e:
        print(f"✗ Browser initialization failed: {e}")
        print("\nPlease install Chrome or Firefox:")
        print("  Ubuntu/Debian:")
        print("    Chrome: sudo apt install google-chrome-stable")
        print("    Firefox: sudo apt install firefox")
        print("\n  You can also set environment variables:")
        print("    BROWSER=firefox  (to explicitly use Firefox)")
        print("    HEADLESS=false   (to disable headless mode)")
        return False

# Configure logging
logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('test_execution.log', mode='w')
    ]
)
logger = logging.getLogger(__name__)


class TestRunner:
    """
    Test runner class to manage execution of all automation tests.
    """
    
    def __init__(self):
        """Initialize test runner with empty results."""
        self.results = []
        self.start_time = None
        self.end_time = None
    
    def run_test(self, test_func, test_name):
        """
        Run a single test and record the result.
        
        Args:
            test_func: Function to execute
            test_name: Name of the test for reporting
        
        Returns:
            bool: True if test passed, False otherwise
        """
        print("\n" + "="*80)
        print(f"Running: {test_name}")
        print("="*80)
        
        start_time = datetime.now()
        try:
            logger.info(f"Starting test: {test_name}")
            success = test_func()
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            self.results.append({
                'name': test_name,
                'status': 'PASSED' if success else 'FAILED',
                'duration': duration,
                'error': None
            })
            
            logger.info(f"Test {test_name} completed: {'PASSED' if success else 'FAILED'}")
            return success
            
        except Exception as e:
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            error_msg = str(e)
            
            self.results.append({
                'name': test_name,
                'status': 'ERROR',
                'duration': duration,
                'error': error_msg
            })
            
            logger.error(f"Test {test_name} error: {error_msg}")
            print(f"\n✗ Error in {test_name}: {error_msg}")
            return False
    
    def run_all_tests(self):
        """
        Run all automation tests in sequence.
        
        Returns:
            bool: True if all tests passed, False otherwise
        """
        self.start_time = datetime.now()
        
        # Ensure screenshots directory exists
        screenshot_utils.ensure_screenshot_dir()
        
        print("\n" + "#"*80)
        print("#" + " "*78 + "#")
        print("#" + " "*20 + "SELENIUM WEBDRIVER LAB 6 - TEST SUITE" + " "*21 + "#")
        print("#" + " "*78 + "#")
        print("#"*80)
        
        # Define all tests to run
        tests = [
            (google_search.google_search_automation, "Google Search Automation"),
            (form_automation.form_automation, "Form Automation"),
            (selectors_demo.selectors_demo, "Selectors Demonstration"),
            (navigation_demo.navigation_demo, "Navigation Demonstration"),
        ]
        
        # Run each test
        for test_func, test_name in tests:
            self.run_test(test_func, test_name)
            print()  # Add spacing between tests
        
        self.end_time = datetime.now()
        return self.generate_report()
    
    def generate_report(self):
        """
        Generate and display test execution report.
        
        Returns:
            bool: True if all tests passed, False otherwise
        """
        total_duration = (self.end_time - self.start_time).total_seconds()
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results if r['status'] == 'PASSED')
        failed_tests = sum(1 for r in self.results if r['status'] == 'FAILED')
        error_tests = sum(1 for r in self.results if r['status'] == 'ERROR')
        
        print("\n" + "="*80)
        print("TEST EXECUTION REPORT")
        print("="*80)
        print(f"\nExecution Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} - "
              f"{self.end_time.strftime('%H:%M:%S')}")
        print(f"Total Duration: {total_duration:.2f} seconds")
        print(f"\nTotal Tests: {total_tests}")
        print(f"Passed: {passed_tests} ✓")
        print(f"Failed: {failed_tests} ✗")
        print(f"Errors: {error_tests} ⚠")
        
        print("\n" + "-"*80)
        print("Individual Test Results:")
        print("-"*80)
        
        for result in self.results:
            status_symbol = {
                'PASSED': '✓',
                'FAILED': '✗',
                'ERROR': '⚠'
            }.get(result['status'], '?')
            
            print(f"\n{status_symbol} {result['name']}")
            print(f"  Status: {result['status']}")
            print(f"  Duration: {result['duration']:.2f}s")
            
            if result['error']:
                print(f"  Error: {result['error']}")
        
        print("\n" + "="*80)
        
        # Summary
        if failed_tests == 0 and error_tests == 0:
            print("✓ ALL TESTS PASSED!")
            print("="*80)
            logger.info("All tests completed successfully")
            return True
        else:
            print(f"✗ SOME TESTS FAILED OR HAD ERRORS")
            print("="*80)
            logger.warning(f"Test suite completed with {failed_tests} failures and {error_tests} errors")
            return False


def main():
    """
    Main entry point for the test suite.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    try:
        # Check browser availability first
        if not check_browser_availability():
            sys.exit(1)
        
        # Create and run test suite
        runner = TestRunner()
        all_passed = runner.run_all_tests()
        
        # Exit with appropriate code
        sys.exit(0 if all_passed else 1)
        
    except KeyboardInterrupt:
        print("\n\nTest execution interrupted by user.")
        logger.warning("Test execution interrupted by user")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n\nUnexpected error in test runner: {str(e)}")
        logger.error(f"Unexpected error in test runner: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
