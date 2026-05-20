import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from locators.home_locators import page_one_xpath, older_newes_letters_xpath, multiple_selt_audix_xpath, multiple_selt_volov_xpath, dropdown_xpath, Text_Area_Field_xpath

import logging
logger = logging.getLogger(__name__)

# from utils.config_reader import get_config
# USERNAME = get_config("LOGIN", "username")
# PASSWORD = get_config("LOGIN", "password")

def test_open_website(driver):
    print("Title of the page is: ", driver.title)
    assert "omayo (QAFox.com)" in driver.title


def test_verify_page_one(driver):
    element = driver.find_element(*page_one_xpath)
    assert element.is_displayed()
    logger.info("Page One is displayed")
    driver.save_screenshot(r"D:\Automation\UI_automation_project\blogspot\screenshot\page_one.png") 

def test_verify_older_news_letter(driver):
    element = driver.find_element(*older_newes_letters_xpath)
    assert element.is_displayed()
    logger.info("Older News Letter dropdown is displayed")
    driver.save_screenshot(r"D:\Automation\UI_automation_project\blogspot\screenshot\older_news_letter.png")       

def test_verify_multiple_selection_audix(driver):
    driver.find_element(*multiple_selt_audix_xpath).click()
    logger.info("Selected Audix option from dropdown")
    driver.save_screenshot(r"D:\Automation\UI_automation_project\blogspot\screenshot\audix_selection.png")
    driver.find_element(*multiple_selt_volov_xpath).click()
    logger.info("Selected Volvox option from dropdown")
    driver.save_screenshot(r"D:\Automation\UI_automation_project\blogspot\screenshot\volov_selection.png")
    time.sleep(3)

def test_dropdown(driver):
    dropdown_element = driver.find_element(*dropdown_xpath)
    logger.info("Clicked on Older News Letter dropdown")
    dropdown = Select(dropdown_element)

    options = ["doc 1", "doc 2", "doc 3", "doc 4"]
    for option in options:
        dropdown.select_by_visible_text(option)
        selected_option = dropdown.first_selected_option.text
        if selected_option == option:
            assert True
            logger.info(f"{option} selected successfully")
        else:
            assert False
            logger.error(f"{option} not selected")

@pytest.mark.grp1
def test_text_area_field(driver):
    driver.find_element(*Text_Area_Field_xpath).send_keys("A garden is a small area where plants like flowers, fruits, or vegetables are grown. It makes the surroundings beautiful and gives fresh air and relaxation.")
    logger.info("Entered text in Text Area Field")    
    driver.save_screenshot(r"D:\Automation\UI_automation_project\blogspot\screenshot\text_area_field.png")        



# def test_navigate_to_practice_page(driver):
#     driver.find_element(*PRACTICE_MENU_xpath).click()
#     logger.info("Clicked on Practice menu")
#     assert "Practice" in driver.title
#     driver.save_screenshot(r"D:\Automation\UI_automation_project\pp\screenshot\practice_page.png")
#     driver.find_element(*LOGIN_PAGE_LINK_xpath).click()
#     logger.info("Clicked on Login link")
#     assert "Test Login" in driver.title
#     driver.save_screenshot(r"D:\Automation\UI_automation_project\pp\screenshot\login_page.png") 
#     driver.find_element(*username_xpath).send_keys(USERNAME)
#     driver.find_element(*password_xpath).send_keys(PASSWORD)
#     driver.find_element(*submit_button_xpath).click()
#     logger.info("Clicked on Submit button")
#     assert "Logged In Successfully" in driver.page_source
#     time.sleep(5)
#     driver.save_screenshot(r"D:\Automation\UI_automation_project\pp\screenshot\login_success.png")

# def test_Test_Exceptions(driver):
#     driver.find_element(*PRACTICE_MENU_xpath).click()
#     driver.find_element(*test_exceptions_xpath).click()
#     driver.find_element(By.xpath, "//button[@id='add_btn']").click()
#     time.sleep(2)

