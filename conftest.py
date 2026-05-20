import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Configure logging
log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)

log_filename = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    """
    Fixture to initialize and teardown WebDriver
    """
    logger.info("=" * 80)
    logger.info("Starting WebDriver initialization")
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    logger.info("WebDriver initialized and page loaded: https://omayo.blogspot.com/")
    logger.info("=" * 80)
    
    yield driver
    
    logger.info("=" * 80)
    logger.info("Closing WebDriver")
    driver.quit()
    logger.info("WebDriver closed successfully")
    logger.info("=" * 80)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Configure pytest to generate HTML reports with date/time format
    """
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(report_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"test_report_{timestamp}.html"
    report_path = os.path.join(report_dir, report_filename)
    
    config.option.htmlpath = report_path
    config.addinivalue_line("markers", "grp1: mark test to run as group 1")
    
    logger.info(f"HTML Report will be generated at: {report_path}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """
    Hook called before each test execution
    """
    logger.info(f"\n{'#' * 80}")
    logger.info(f"TEST STARTED: {item.name}")
    logger.info(f"{'#' * 80}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and add logs
    """
    if call.when == "setup":
        logger.info(f"[SETUP] Setting up test: {item.name}")
    elif call.when == "call":
        if call.excinfo is None:
            logger.info(f"[EXECUTION] Test passed: {item.name}")
        else:
            logger.error(f"[EXECUTION] Test failed: {item.name}")
            logger.error(f"Exception: {call.excinfo.value}")
    elif call.when == "teardown":
        logger.info(f"[TEARDOWN] Tearing down test: {item.name}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """
    Hook called after test execution to log results
    """
    if report.when == "call":
        if report.outcome == "passed":
            logger.info(f"[PASSED] TEST PASSED: {report.nodeid}")
        elif report.outcome == "failed":
            logger.error(f"[FAILED] TEST FAILED: {report.nodeid}")
            if report.longrepr:
                logger.error(f"Failure Details: {report.longrepr}")
        elif report.outcome == "skipped":
            logger.warning(f"[SKIPPED] TEST SKIPPED: {report.nodeid}")
    
    if report.when == "teardown":
        logger.info(f"{'*' * 80}\n")


@pytest.fixture(scope="session", autouse=True)
def session_finalize(request):
    """
    Session-level fixture for cleanup and final logging
    """
    def fin():
        logger.info("\n" + "=" * 80)
        logger.info("TEST SESSION COMPLETED")
        logger.info(f"Log file saved at: {log_filename}")
        logger.info("=" * 80 + "\n")
    
    request.addfinalizer(fin)
