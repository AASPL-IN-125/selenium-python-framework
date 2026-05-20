# Blogspot UI Automation Framework

A comprehensive Selenium-based UI automation framework for testing Blogspot (https://omayo.blogspot.com/) with integrated HTML reporting and enhanced logging capabilities.

## Project Overview

This project is a professional UI automation framework built with:
- **Selenium WebDriver** for browser automation
- **pytest** as the testing framework
- **pytest-html** for HTML report generation
- **Comprehensive Logging** with test lifecycle tracking
- **Date/Time Timestamped Reports** for easy tracking
- **Screenshot Capture** on test execution

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Reports & Logs](#reports--logs)
- [Project Components](#project-components)
- [Test Cases](#test-cases)
- [Logging & Reports](#logging--reports)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Features

✅ **Automated Browser Testing** - Full browser automation with Selenium WebDriver  
✅ **HTML Report Generation** - Auto-generated reports with timestamp format  
✅ **Enhanced Logging** - Comprehensive logs for all test phases (setup, execution, teardown)  
✅ **Test Hooks** - Pytest hooks for capturing test results (Pass/Fail/Skip)  
✅ **Screenshot Capture** - Automatic screenshot capture during test execution  
✅ **Date/Time Tracking** - All reports and logs include date/time stamps (YYYYMMDD_HHMMSS)  
✅ **Configurable Settings** - Easy configuration via config.ini  
✅ **Element Locators** - Centralized XPath/CSS selectors management  
✅ **Modular Architecture** - Clean separation of concerns (tests, locators, pages, utils)  

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python** 3.10 or higher
- **pip** (Python package manager)
- **Google Chrome** browser (for ChromeDriver)
- **Git** (for version control)
- **Virtual Environment** support (included with Python)

---

## Project Structure

```
blogspot/
├── conftest.py                 # Pytest configuration and fixtures with logging/reporting
├── pytest.ini                  # Pytest configuration file
├── requirements.txt            # Project dependencies
├── REPORT_GUIDE.md            # Detailed reporting and logging documentation
├── flow.md                     # Application flow diagrams with Mermaid
├── README.md                   # This file
├── config/
│   ├── __init__.py
│   └── config.ini             # Configuration settings
├── locators/
│   ├── __init__.py
│   └── home_locators.py       # Web element locators (XPath/CSS)
├── pages/
│   └── __init__.py            # Page Object classes
├── tests/
│   ├── __init__.py
│   ├── test_ok.py             # Main test cases
│   ├── test_rt.py             # Additional test cases
│   └── logs/                  # Test session logs
├── utils/
│   ├── __init__.py
│   └── config_reader.py       # Configuration reader utility
├── logs/                       # Test execution logs with timestamps
├── reports/                    # HTML test reports with timestamps
│   └── assets/
│       └── style.css          # Report styling
├── screenshot/                 # Screenshots captured during tests
└── test_data/                 # Test data files
    └── __init__.py
```

---

## Setup & Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/AASPL-IN-125/selenium-python-framework.git
cd blogspot
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

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

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Core Dependencies:**
- selenium>=4.0.0
- pytest>=7.0.0
- pytest-html>=3.1.0
- pytest-xdist>=3.0.0
- webdriver-manager>=3.8.0

---

## Configuration

### config/config.ini

This file contains all configuration settings used by the automation framework:

```ini
[DEFAULT]
base_url = https://omayo.blogspot.com/

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
pytest tests/test_ok.py -v -s
```

### Run with Verbose Output

```bash
pytest -v tests/
```

### Run with Logs Display in Console

```bash
pytest -v -s tests/test_ok.py
```

### Run Specific Test Case

```bash
pytest tests/test_ok.py::test_open_website -v
```

### Run Tests with HTML Report (Auto-generated)

The HTML report is automatically generated with every test run:

```bash
pytest tests/ -v -s
```

**Report Location**: `reports/test_report_YYYYMMDD_HHMMSS.html`

### Run with Specific Markers

```bash
pytest tests/ -m grp1 -v -s
```

### Run Tests with Short Traceback

```bash
pytest tests/ -v -s --tb=short
```

---

## Reports & Logs

### Automatic Report Generation

Every test execution automatically generates:

1. **HTML Report** - Visual test results report
   - Location: `reports/test_report_YYYYMMDD_HHMMSS.html`
   - Format: Timestamp-based filename (e.g., `test_report_20260520_153844.html`)
   - Content: Test summary, detailed results, logs, execution times

2. **Log File** - Detailed execution logs
   - Location: `logs/test_log_YYYYMMDD_HHMMSS.log`
   - Format: Plain text with timestamps
   - Content: All test phases (setup, execution, teardown), assertions, errors

### Viewing Reports

1. **Open HTML Report in Browser:**
   ```bash
   # Windows
   start reports/test_report_20260520_153844.html
   
   # macOS
   open reports/test_report_20260520_153844.html
   
   # Linux
   firefox reports/test_report_20260520_153844.html
   ```

2. **View Log File in Text Editor:**
   - Windows: Open with Notepad or VS Code
   - macOS/Linux: Open with any text editor

### Log Format

Each log entry includes timestamp, log level, module, and message:

```
2026-05-20 15:38:44,466 - conftest - INFO - HTML Report will be generated at: D:\...\reports\test_report_20260520_153844.html
2026-05-20 15:38:51,837 - conftest - INFO - WebDriver initialized and page loaded: https://omayo.blogspot.com/
2026-05-20 15:38:51,859 - conftest - INFO - [EXECUTION] Test passed: test_open_website
2026-05-20 15:39:02,406 - tests.test_ok - INFO - Page One is displayed
```

### Log Phases

Logs are organized by test phases:

- **[SETUP]** - Test initialization and setup phase
- **[EXECUTION]** - Main test execution and assertions
- **[TEARDOWN]** - Test cleanup and driver teardown
- **[PASSED]** - Successful test execution
- **[FAILED]** - Failed test execution with error details
- **[SKIPPED]** - Skipped test execution

---

## Project Components

### 1. **conftest.py** - Pytest Configuration & Fixtures

Enhanced with comprehensive logging and report generation:

**Features:**
- WebDriver fixture for Chrome browser setup/teardown
- Automatic HTML report generation with timestamp
- Integrated logging for all test phases
- Pytest hooks for capturing test results
- Session-level cleanup and finalization

**WebDriver Fixture:**
```python
@pytest.fixture
def driver():
    """Initialize WebDriver and navigate to application"""
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
```

**Report Hook:**
```python
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure HTML report generation with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"test_report_{timestamp}.html"
    config.option.htmlpath = os.path.join(report_dir, report_filename)
```

### 2. **pytest.ini** - Pytest Configuration

```ini
[pytest]
# Logging Configuration
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s - %(levelname)s - [%(name)s] - %(message)s

log_file = logs/test.log
log_file_level = INFO

# Markers
markers =
    grp1: Group 1 tests

# Test Discovery
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### 3. **locators/home_locators.py** - Web Element Locators

Contains centralized XPath and CSS selectors:

```python
from selenium.webdriver.common.by import By

page_one_xpath = (By.XPATH, "//h3[@class='post-title entry-title']")
older_newes_letters_xpath = (By.XPATH, "//select[@id='drop1']")
multiple_selt_audix_xpath = (By.XPATH, "//option[@value='audix']")
dropdown_xpath = (By.XPATH, "//select[@id='drop1']")
Text_Area_Field_xpath = (By.XPATH, "//textarea[@id='ta1']")
```

### 4. **utils/config_reader.py** - Configuration Manager

Utility to read configuration values from `config.ini`:

```python
from utils.config_reader import get_config

username = get_config("LOGIN", "username")
base_url = get_config("DEFAULT", "base_url")
```

---

## Test Cases

### Test Files: test_ok.py

#### test_open_website()
- **Purpose**: Verify website loads correctly
- **Steps**: Navigate to URL and check page title
- **Expected**: Page title contains "omayo (QAFox.com)"
- **Logs**: Page title verification logged

#### test_verify_page_one()
- **Purpose**: Verify Page One element is displayed
- **Steps**: Find element by XPath and check visibility
- **Expected**: Element is displayed
- **Logs**: Element visibility logged
- **Screenshot**: `page_one.png`

#### test_verify_older_news_letter()
- **Purpose**: Verify dropdown element is present
- **Steps**: Locate dropdown and verify display
- **Expected**: Dropdown is visible
- **Screenshot**: `older_news_letter.png`

#### test_verify_multiple_selection_audix()
- **Purpose**: Test multiple element selections
- **Steps**: 
  1. Click Audix option
  2. Click Volvox option
  3. Wait 3 seconds
- **Screenshots**: `audix_selection.png`, `volov_selection.png`

#### test_dropdown()
- **Purpose**: Test dropdown option selection
- **Steps**: Select multiple options (doc 1, doc 2, doc 3, doc 4)
- **Expected**: Each option selects successfully
- **Logs**: Each selection logged with [PASSED] status
- **Marker**: grp1

#### test_text_area_field()
- **Purpose**: Test text input in textarea
- **Steps**: Enter multi-line text in textarea
- **Expected**: Text entered successfully
- **Screenshot**: `text_area_field.png`
- **Marker**: @pytest.mark.grp1

---

## Logging & Reports

### Logging Levels

- **INFO**: General information about test execution
- **WARNING**: Warning messages (skipped tests, non-critical issues)
- **ERROR**: Error messages and failure details

### Logging in Test Files

```python
import logging

logger = logging.getLogger(__name__)

def test_example(driver):
    logger.info("Starting test execution")
    element = driver.find_element(*locator)
    logger.info("Element found successfully")
    assert element.is_displayed()
    logger.info("Element is displayed - PASSED")
```

### Accessing Reports & Logs

**List Latest Reports:**
```powershell
Get-ChildItem reports/*.html | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

**List Latest Logs:**
```powershell
Get-ChildItem logs/*.log | Sort-Object LastWriteTime -Descending | Select-Object -First 5
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
- Log important test steps for easy debugging
- Capture screenshots on failures
- Use verbose logging for troubleshooting
- Review reports and logs after test runs

### 4. **Test Data Management**
- Keep test data in `test_data/` directory
- Use configuration files for dynamic values
- Separate test data from test logic

### 5. **Test Organization**
- Group related tests with markers (e.g., `@pytest.mark.grp1`)
- Use descriptive test names
- Add docstrings to test functions
- Keep tests independent and atomic

### 6. **Report Management**
- Review HTML reports after each test run
- Archive reports for audit trails
- Share reports with stakeholders
- Use timestamps for easy tracking

---

## Troubleshooting

### Issue: No Report Generated

**Solution:**
```bash
# Verify pytest-html is installed
pip install pytest-html

# Ensure reports directory exists
mkdir reports

# Run tests with explicit report option
pytest tests/ -v -s
```

### Issue: Logs Not Appearing in Console

**Solution:**
- Check log_cli_level in pytest.ini is set to INFO
- Verify conftest.py has logging configured
- Run with verbose flag: `pytest -v -s`

### Issue: WebDriver Not Found

**Solution:**
```bash
# Update webdriver-manager
pip install --upgrade webdriver-manager

# Run tests (webdriver-manager will auto-download ChromeDriver)
pytest tests/
```

### Issue: Unicode Encoding Errors

**Solution:**
- This is typically a Windows console encoding issue
- Run tests within VS Code integrated terminal
- Or use Python's UTF-8 mode: `python -m pytest tests/`

### Issue: Test Hangs or Times Out

**Solution:**
- Check internet connection (tests navigate to external URL)
- Increase browser loading wait time
- Check if website is accessible: https://omayo.blogspot.com/

---

## Additional Resources

- [Selenium Documentation](https://selenium.dev/documentation/)
- [pytest Documentation](https://docs.pytest.org/)
- [pytest-html Plugin](https://pytest-html.readthedocs.io/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

## Version History

### v1.1.0 (2026-05-20)
- ✅ Added HTML report generation with timestamp format
- ✅ Enhanced logging with test lifecycle tracking
- ✅ Added pytest hooks for result capturing
- ✅ Created comprehensive documentation (REPORT_GUIDE.md, flow.md)
- ✅ Updated conftest.py with logging configuration
- ✅ Fixed Unicode encoding issues
- ✅ Added requirements.txt

### v1.0.0 (Initial Release)
- ✅ Basic test automation framework
- ✅ Locator management
- ✅ Configuration management
- ✅ Utility functions

---

## License

This project is licensed under the MIT License - see LICENSE file for details.

---

## Authors

- **Project**: Blogspot UI Automation Framework
- **Repository**: [AASPL-IN-125/selenium-python-framework](https://github.com/AASPL-IN-125/selenium-python-framework)

---

## Support

For issues or questions:
1. Check the [REPORT_GUIDE.md](REPORT_GUIDE.md) for detailed reporting documentation
2. Review [flow.md](flow.md) for application flow diagrams
3. Check test logs in `logs/` directory
4. Review HTML reports in `reports/` directory

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
