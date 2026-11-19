import logging

from pages.home_page import HomePage

logger = logging.getLogger(__name__)

EXPECTED_HOME_PAGE_TITLE = "Practice Test Automation | Learn Selenium WebDriver"


def test_open_home_page(driver, base_url):
    home_page = HomePage(driver)
    home_page.open(base_url)
    logger.info(f"Opened home page: {base_url}")

    actual_title = home_page.get_title()
    logger.info(f"Home page title: {actual_title}")
    assert actual_title == EXPECTED_HOME_PAGE_TITLE
