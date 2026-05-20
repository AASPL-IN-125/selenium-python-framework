import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    # driver.save_screenshot(r"D:\Automation\UI_automation_project\pp\screenshot\home_page.png")
    yield driver
    driver.quit()


    