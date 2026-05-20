# UI Automation Project - Practice Test Automation

## Project Overview

This is a Selenium-based UI automation framework designed to automate and test the user interface of **Practice Test Automation** (https://practicetestautomation.com/). The project follows the **Page Object Model (POM)** pattern and uses **pytest** as the testing framework.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Project Components](#project-components)
- [Test Cases](#test-cases)
- [Logging & Reports](#logging--reports)
- [Best Practices](#best-practices)

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python** (3.7 or higher)
- **pip** (Python package manager)
- **Google Chrome** browser
- **Git** (optional, for version control)

---

## Project Structure

```
practicetestautomation/
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                  # Pytest configuration file
├── config/
│   ├── __init__.py
│   └── config.ini             # Configuration settings (base URL, credentials)
├── locators/
│   ├── __init__.py
│   └── home_locators.py       # Web element locators using XPath/CSS
├── pages/
│   └── __init__.py            # Page Object classes (if implemented)
├── tests/
│   ├── __init__.py
│   ├── test_ui.py             # Main UI test cases
│   ├── test_rt.py             # Additional test cases
│   └── logs/                  # Test execution logs
├── utils/
│   ├── __init__.py
│   └── config_reader.py       # Configuration reader utility
├── logs/                       # Test execution logs
├── reports/                    # Test reports
│   └── assets/
│       └── style.css          # Report styling
├── screenshot/                 # Screenshots captured during tests
└── test_data/                 # Test data files
    └── __init__.py
```

---

## Setup & Installation

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**If requirements.txt is not available, install these packages:**

```bash
pip install selenium
pip install pytest
pip install webdriver-manager
pip install configparser
```

---

## Configuration

### config/config.ini

This file contains all configuration settings used by the automation framework:

```ini
[DEFAULT]
base_url = https://practicetestautomation.com/

[LOGIN]
username = student
password = Password123
```

**How to Use:**
- The `config_reader.py` utility reads these values
- Access config values in test files using: `get_config("SECTION", "key")`

---

## Running Tests

### Run All Tests

```bash
pytest tests/
```

### Run Specific Test File

```bash
pytest tests/test_ui.py -v
```

### Run with Verbose Output

```bash
pytest -v tests/
```

### Run with Logs Display in Console

```bash
pytest -v -s tests/test_ui.py
```

### Run Specific Test Case

```bash
pytest tests/test_ui.py::test_navigate_to_practice_page -v
```

### Run Tests with HTML Report

```bash
pytest tests/ --html=reports/report.html
```

---

## Project Components

### 1. **conftest.py** - Pytest Fixtures

Defines common fixtures used across test files:

- **driver**: Creates a Chrome WebDriver instance
  - Navigates to the base URL
  - Maximizes the browser window
  - Provides teardown for cleanup

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/")
    driver.maximize_window()
    yield driver
    return driver
```

### 2. **locators/home_locators.py** - Web Element Locators

Contains XPath and CSS selectors for all web elements:

```python
PRACTICE_MENU_xpath = (By.XPATH, "//a[text()='Practice']")
LOGIN_PAGE_LINK_xpath = (By.XPATH, "//a[@href='...']")
username_xpath = (By.XPATH, "//input[@name='username']")
password_xpath = (By.XPATH, "//input[@name='password']")
submit_button_xpath = (By.XPATH, "//button[@class='btn']")
```

**Best Practice**: Keep all locators in a separate file for easy maintenance.

### 3. **utils/config_reader.py** - Configuration Manager

Utility to read configuration values from `config.ini`:

```python
from utils.config_reader import get_config

username = get_config("LOGIN", "username")
password = get_config("LOGIN", "password")
```

### 4. **pytest.ini** - Pytest Configuration

Configures pytest behavior:

```ini
[pytest]
log_cli = true                          # Display logs in console
log_cli_level = INFO                    # Log level
log_file = logs/test.log               # Log file location
log_file_level = INFO
log_file_format = %(asctime)s - %(levelname)s - %(message)s
```

---

## Test Cases

### test_navigate_to_practice_page()

**Purpose**: Tests the complete login flow

**Steps**:
1. Click on "Practice" menu
2. Navigate to Login page
3. Enter username and password
4. Submit login form
5. Verify successful login

**Expected Result**: "Logged In Successfully" message appears on page

**Screenshots Captured**:
- practice_page.png
- login_page.png
- login_success.png

---

## Logging & Reports

### Logs Location

- **Console Logs**: Displayed in terminal during test execution
- **File Logs**: `logs/test.log` - Contains all execution details
- **Screenshots**: `screenshot/` - Captured during test execution
- **Reports**: `reports/` - Test execution reports

### Log Format

```
2026-05-19 10:30:45 - INFO - Clicked on Practice menu
2026-05-19 10:30:46 - INFO - Clicked on Login link
2026-05-19 10:30:47 - INFO - Clicked on Submit button
```

### Accessing Logs in Code

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Test step message")
logger.warning("Warning message")
logger.error("Error message")
```

---

## Best Practices

### 1. **Page Object Model (POM)**
- Keep all locators in separate files
- Create page classes for better organization
- Avoid hardcoding locators in test files

### 2. **Configuration Management**
- Use `config.ini` for environment-specific settings
- Never hardcode credentials in test files
- Store sensitive data securely

### 3. **Logging & Debugging**
- Log important test steps
- Capture screenshots on failures
- Use verbose logging for troubleshooting

### 4. **Test Data Management**
- Keep test data in `test_data/` directory
- Use configuration files for dynamic data
- Avoid hardcoding test data in test files

### 5. **Fixture Usage**
- Use pytest fixtures for setup and teardown
- Create reusable fixtures for common operations
- Keep fixtures in `conftest.py`

### 6. **Test Organization**
- Group related tests in separate files
- Use meaningful test function names
- Keep tests independent and isolated

### 7. **Element Locators**
- Prefer XPath/CSS selectors that are stable
- Avoid brittle selectors based on element position
- Use meaningful variable names for locators

---

## Common Issues & Solutions

### Issue: Chrome Driver Not Found
**Solution**:
```bash
pip install webdriver-manager
```
The `webdriver-manager` package automatically downloads the correct Chrome driver version.

### Issue: Tests Cannot Find config.ini
**Solution**: Ensure you're running tests from the project root directory:
```bash
cd d:\Automation\UI_automation_project\practicetestautomation
pytest tests/
```

### Issue: Element Not Found
**Solution**:
1. Verify the XPath/CSS selector is correct
2. Add explicit waits before clicking elements
3. Check if the element is visible/interactable
4. Update locators if the website has changed

### Issue: Permission Denied on Virtual Environment
**Solution** (Windows PowerShell):
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

---

## Troubleshooting

### Debug Mode
Run tests with additional output:
```bash
pytest -vvs tests/
```

### Run Single Test with Debugging
```bash
pytest tests/test_ui.py::test_navigate_to_practice_page -vvs --tb=short
```

### Check Logs
```bash
cat logs/test.log
```

---

## Next Steps

1. **Expand Test Coverage**: Add more test cases for different scenarios
2. **Create Page Classes**: Implement page object classes in `pages/` directory
3. **Add Test Data**: Create test data files for different user roles
4. **Implement Retry Logic**: Add retry mechanism for flaky tests
5. **Generate Reports**: Integrate HTML report generation
6. **CI/CD Integration**: Set up GitHub Actions or Jenkins for automated testing

---

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Practice Test Automation Website](https://practicetestautomation.com/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

## Author & Support

For questions or issues, please refer to the project documentation or contact the development team.

---

**Last Updated**: May 19, 2026
