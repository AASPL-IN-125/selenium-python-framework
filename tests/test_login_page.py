import logging

from locators.practice_locators import (
    home_menu_xpath,
    practice_menu_xpath,
    test_login_page_link_xpath,
    login_success_heading_xpath,
    logout_button_xpath,
)
from tests.login_test_case import login_test_case
from utils.config_reader import get_username, get_password

logger = logging.getLogger(__name__)

USERNAME = get_username()
PASSWORD = get_password()


def test_login_page(driver, base_url):
    driver.get(base_url)
    driver.find_element(*home_menu_xpath).click()
    logger.info("Clicked on Home menu")

    driver.find_element(*practice_menu_xpath).click()
    logger.info("Clicked on Practice menu")
    assert "practice" in driver.current_url

    driver.find_element(*test_login_page_link_xpath).click()
    logger.info("Clicked on Test Login Page link")
    assert "practice-test-login" in driver.current_url

    login_test_case(driver, USERNAME, PASSWORD)

    assert "logged-in-successfully" in driver.current_url
    assert driver.find_element(*login_success_heading_xpath).is_displayed()
    assert driver.find_element(*logout_button_xpath).is_displayed()
    logger.info("Logged in successfully")
