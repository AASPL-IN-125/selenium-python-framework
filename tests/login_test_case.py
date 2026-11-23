import logging

from locators.practice_locators import username_xpath, password_xpath, submit_button_xpath

logger = logging.getLogger(__name__)


def login_test_case(driver, username, password):
    driver.find_element(*username_xpath).send_keys(username)
    logger.info(f"Entered username: {username}")
    driver.find_element(*password_xpath).send_keys(password)
    logger.info("Entered password")
    driver.find_element(*submit_button_xpath).click()
    logger.info("Clicked on Submit button")
