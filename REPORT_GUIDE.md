# HTML Report Configuration Guide

## Overview
The test automation framework has been updated to generate comprehensive HTML reports with integrated logging for each test case.

## Features

### 1. **HTML Report Generation**
- Reports are automatically generated after test execution
- Report files are saved in the `reports/` folder
- File naming format: `test_report_YYYYMMDD_HHMMSS.html`
- Each report includes:
  - Test execution summary
  - Pass/Fail statistics
  - Individual test details
  - Logs for each test case
  - Execution timestamps

### 2. **Integrated Logging**
- Logs are captured for the entire test session
- Log files are saved in the `logs/` folder
- File naming format: `test_log_YYYYMMDD_HHMMSS.log`
- Log levels: INFO, ERROR, WARNING
- Logs include:
  - Test setup information
  - Test execution details
  - Test results (Pass/Fail/Skip)
  - Driver initialization/teardown
  - Exception details for failed tests

### 3. **Log Markers**
Logs include clear markers for each phase:
- `[SETUP]` - Test setup phase
- `[EXECUTION]` - Test execution phase
- `[TEARDOWN]` - Test teardown phase
- `✅ PASSED` - Successful tests
- `❌ FAILED` - Failed tests
- `⊘ SKIPPED` - Skipped tests

## Running Tests

### Basic Test Execution
```bash
pytest tests/
```

### Verbose Output with HTML Report
```bash
pytest tests/ -v -s
```

### Run Specific Test File
```bash
pytest tests/test_ok.py -v -s
```

### Run Tests with Specific Marker
```bash
pytest tests/ -m grp1 -v -s
```

## Report Locations

### HTML Reports
Location: `reports/test_report_YYYYMMDD_HHMMSS.html`
- Open in web browser to view comprehensive test report
- Includes timings, logs, and screenshots

### Log Files
Location: `logs/test_log_YYYYMMDD_HHMMSS.log`
- Plain text format
- Can be viewed in any text editor
- Useful for debugging and troubleshooting

## Configuration Files

### conftest.py
- Pytest fixture configuration
- Report generation setup
- Logging configuration
- Test lifecycle hooks

### pytest.ini
- Pytest settings
- Logging levels
- Test discovery patterns
- Default command-line options

### requirements.txt
- Project dependencies
- pytest-html for report generation
- selenium for web automation

## Example Report Structure

```
Test Report Summary
├── Passed: 6
├── Failed: 0
├── Skipped: 0
└── Duration: 45.23s

Test Cases
├── test_open_website
│   ├── Status: PASSED
│   ├── Duration: 2.34s
│   └── Logs: [captured logs]
├── test_verify_page_one
│   ├── Status: PASSED
│   ├── Duration: 1.89s
│   └── Logs: [captured logs]
└── ... (other tests)
```

## Troubleshooting

### No Report Generated
- Verify pytest-html is installed: `pip install pytest-html`
- Check `reports/` folder exists
- Review pytest.ini configuration

### Logs Not Appearing in Report
- Ensure logging is configured in conftest.py
- Check log_cli_level in pytest.ini
- Verify logger usage in test files

### Report File Path Issues
- Reports are saved with absolute path from conftest.py
- Default location: `{project_root}/reports/`
- Can be customized in conftest.py pytest_configure hook

## Best Practices

1. **Review Reports After Tests**
   - Check HTML reports for test failures
   - Use logs for detailed debugging

2. **Archive Old Reports**
   - Date/time format helps identify reports
   - Consider archiving old reports periodically

3. **Sharing Reports**
   - HTML reports are standalone files
   - Can be sent via email or shared on network
   - Include corresponding log files for reference

4. **CI/CD Integration**
   - Reports can be published to CI/CD dashboards
   - Logs can be archived for audit trails
   - Timestamps help track test trends

## Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-html Plugin](https://pytest-html.readthedocs.io/)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
