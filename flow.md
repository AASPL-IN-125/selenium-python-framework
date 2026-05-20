# UI Automation Flow Documentation

This document provides comprehensive flow diagrams for the Blogspot UI Automation project using Mermaid diagrams.

---

## 1. Overall Project Architecture

```mermaid
graph TB
    subgraph Project["Project Structure"]
        Config["📋 Config<br/>(config.ini)"]
        Locators["🎯 Locators<br/>(home_locators.py)"]
        Pages["📄 Pages"]
        Utils["🛠️ Utils<br/>(config_reader.py)"]
        Tests["🧪 Tests<br/>(test_ok.py, test_rt.py)"]
        Conftest["⚙️ Conftest<br/>(Fixtures)"]
    end
    
    subgraph Output["Output"]
        Logs["📝 Logs"]
        Reports["📊 Reports"]
        Screenshots["📸 Screenshots"]
    end
    
    Config -->|Read Configuration| Utils
    Locators -->|Element Locators| Tests
    Pages -->|Page Objects| Tests
    Utils -->|Config Values| Tests
    Conftest -->|Driver Setup| Tests
    Tests -->|Generate| Logs
    Tests -->|Generate| Screenshots
    Tests -->|Generate| Reports
    
    style Project fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    style Output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    style Config fill:#c8e6c9,stroke:#1b5e20
    style Locators fill:#ffe0b2,stroke:#e65100
    style Pages fill:#f8bbd0,stroke:#880e4f
    style Utils fill:#d1c4e9,stroke:#311b92
    style Tests fill:#ffccbc,stroke:#bf360c
    style Conftest fill:#b3e5fc,stroke:#01579b
```

---

## 2. Test Execution Flow

```mermaid
graph TD
    Start([🚀 Start Test Run]) -->|pytest| Config["Load pytest.ini"]
    Config --> Conftest["Execute conftest.py"]
    Conftest --> DriverSetup["Initialize WebDriver"]
    DriverSetup --> LaunchApp["Launch https://omayo.blogspot.com/"]
    LaunchApp --> MaxWindow["Maximize Browser Window"]
    MaxWindow --> TestSelection["Select Tests to Execute"]
    
    TestSelection --> Test1["test_open_website"]
    TestSelection --> Test2["test_verify_page_one"]
    TestSelection --> Test3["test_verify_older_news_letter"]
    TestSelection --> Test4["test_verify_multiple_selection_audix"]
    TestSelection --> Test5["test_dropdown"]
    TestSelection --> Test6["test_text_area_field"]
    
    Test1 -->|PASS/FAIL| Results["Collect Results"]
    Test2 -->|PASS/FAIL| Results
    Test3 -->|PASS/FAIL| Results
    Test4 -->|PASS/FAIL| Results
    Test5 -->|PASS/FAIL| Results
    Test6 -->|PASS/FAIL| Results
    
    Results --> Cleanup["Cleanup - driver.quit()"]
    Cleanup --> End([✅ Test Run Complete])
    
    style Start fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style End fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style DriverSetup fill:#2196f3,stroke:#01579b,color:#fff,stroke-width:2px
    style Cleanup fill:#ff5722,stroke:#bf360c,color:#fff,stroke-width:2px
    style Results fill:#ff9800,stroke:#e65100,color:#fff,stroke-width:2px
```

---

## 3. Driver Initialization Flow

```mermaid
sequenceDiagram
    participant Pytest
    participant Conftest
    participant WebDriver
    participant Browser
    participant Website
    
    Pytest->>Conftest: Call @pytest.fixture
    Conftest->>WebDriver: webdriver.Chrome()
    WebDriver->>Browser: Initialize Chrome
    Browser-->>WebDriver: Chrome Ready
    WebDriver-->>Conftest: Driver Instance
    Conftest->>Website: driver.get(URL)
    Website->>Browser: Load https://omayo.blogspot.com/
    Browser-->>Website: Page Loaded
    Conftest->>Browser: driver.maximize_window()
    Browser-->>Conftest: Window Maximized
    Conftest-->>Pytest: Yield Driver
    Pytest->>Pytest: Execute Test
    Pytest->>Conftest: Test Complete
    Conftest->>Browser: driver.quit()
    Browser-->>Conftest: Browser Closed
    
    style Pytest fill:#e3f2fd,stroke:#1565c0
    style Conftest fill:#fff3e0,stroke:#e65100
    style WebDriver fill:#f3e5f5,stroke:#6a1b9a
    style Browser fill:#e0f2f1,stroke:#00695c
    style Website fill:#fce4ec,stroke:#c2185b
```

---

## 4. Test: Open Website

```mermaid
graph LR
    A["🌐 test_open_website"] --> B["Get driver.title"]
    B --> C["Verify Title Contains<br/>'omayo QAFox.com'"]
    C --> D{Assertion<br/>Passes?}
    D -->|Yes| E["✅ PASS"]
    D -->|No| F["❌ FAIL"]
    
    style A fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style E fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style F fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
    style D fill:#ffc107,stroke:#f57f17,stroke-width:2px
```

---

## 5. Test: Verify Page One Element

```mermaid
graph TD
    A["🔍 test_verify_page_one"] --> B["Find Element by XPath<br/>//h3[@class='post-title entry-title']"]
    B --> C["Check is_displayed()"]
    C --> D{Element<br/>Visible?}
    D -->|Yes| E["✅ Assert True"]
    D -->|No| F["❌ Assert False"]
    E --> G["🖼️ Save Screenshot<br/>page_one.png"]
    F --> H["Log Error"]
    G --> I["📝 Log Info"]
    I --> J["✅ PASS"]
    H --> K["❌ FAIL"]
    
    style A fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style B fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style C fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style D fill:#ffc107,stroke:#f57f17,stroke-width:2px
    style J fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style K fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
```

---

## 6. Test: Verify Older News Letter Dropdown

```mermaid
graph LR
    A["📋 test_verify_older_news_letter"] --> B["Find Element<br/>//select[@id='drop1']"]
    B --> C["Check is_displayed()"]
    C --> D{Dropdown<br/>Found?}
    D -->|Yes| E["✅ Assert True"]
    D -->|No| F["❌ Assert False"]
    E --> G["🖼️ Save Screenshot<br/>older_news_letter.png"]
    F --> H["Log Error"]
    G --> I["📝 Log Info"]
    I --> J["✅ PASS"]
    H --> K["❌ FAIL"]
    
    style A fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style E fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style F fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
    style D fill:#ffc107,stroke:#f57f17,stroke-width:2px
```

---

## 7. Test: Multiple Selection Flow

```mermaid
graph TD
    Start["🎯 test_verify_multiple_selection_audix"] --> Step1["Click Audix Option<br/>//option[@value='audix']"]
    Step1 --> Log1["📝 Log: 'Selected Audix'"]
    Log1 --> Screenshot1["🖼️ Save<br/>audix_selection.png"]
    
    Screenshot1 --> Step2["Click Volvox Option<br/>//option[@value='volvox']"]
    Step2 --> Log2["📝 Log: 'Selected Volvox'"]
    Log2 --> Screenshot2["🖼️ Save<br/>volov_selection.png"]
    
    Screenshot2 --> Wait["⏱️ Wait 3 seconds"]
    Wait --> End["✅ PASS"]
    
    style Start fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Step1 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Step2 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style End fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style Wait fill:#ffc107,stroke:#f57f17,stroke-width:2px
```

---

## 8. Test: Dropdown Selection Flow

```mermaid
graph TD
    Start["📌 test_dropdown"] --> GetDropdown["Find Dropdown Element<br/>//select[@id='drop1']"]
    GetDropdown --> CreateSelect["Create Select Object<br/>using Selenium Select"]
    CreateSelect --> OptionLoop["Loop Through Options"]
    
    OptionLoop --> Option1["Select: 'doc 1'"]
    Option1 --> Check1{"First Option<br/>= 'doc 1'?"}
    Check1 -->|Yes| Pass1["✅ Assert True<br/>📝 Log Success"]
    Check1 -->|No| Fail1["❌ Assert False<br/>📝 Log Error"]
    
    Pass1 --> Option2["Select: 'doc 2'"]
    Fail1 --> Option2
    Option2 --> Check2{"First Option<br/>= 'doc 2'?"}
    Check2 -->|Yes| Pass2["✅ Assert True"]
    Check2 -->|No| Fail2["❌ Assert False"]
    
    Pass2 --> Option3["Select: 'doc 3'"]
    Fail2 --> Option3
    Option3 --> Check3{"First Option<br/>= 'doc 3'?"}
    Check3 -->|Yes| Pass3["✅ Assert True"]
    Check3 -->|No| Fail3["❌ Assert False"]
    
    Pass3 --> Option4["Select: 'doc 4'"]
    Fail3 --> Option4
    Option4 --> Check4{"First Option<br/>= 'doc 4'?"}
    Check4 -->|Yes| Pass4["✅ PASS"]
    Check4 -->|No| Fail4["❌ FAIL"]
    
    style Start fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style CreateSelect fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style Pass1 fill:#c8e6c9,stroke:#1b5e20,stroke-width:1.5px
    style Fail1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:1.5px
    style Pass4 fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style Fail4 fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
```

---

## 9. Test: Text Area Field Input Flow

```mermaid
graph LR
    Start["📝 test_text_area_field<br/>@pytest.mark.grp1"] --> Find["Find Text Area<br/>//textarea[@id='ta1']"]
    Find --> Input["Send Keys:<br/>Long Text about Garden"]
    Input --> Log["📝 Log Info:<br/>Text Area Filled"]
    Log --> Screenshot["🖼️ Save Screenshot<br/>text_area_field.png"]
    Screenshot --> End["✅ PASS"]
    
    style Start fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Find fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Input fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style Screenshot fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style End fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
```

---

## 10. Element Interaction Flow

```mermaid
stateDiagram-v2
    [*] --> Initialize: Page Loaded
    Initialize --> LocateElement: Find Element by Locator
    LocateElement --> ElementFound: Element Retrieved
    ElementFound --> ValidateState: Check Element State
    ValidateState --> StateCheck: is_displayed()?
    
    StateCheck --> Displayed: Yes
    StateCheck --> NotDisplayed: No
    
    Displayed --> Interact: Perform Action
    NotDisplayed --> LogError: Log Error & Fail Test
    
    Interact --> ClickAction: Click/SendKeys/Select
    ClickAction --> CaptureResult: Get Result/State
    CaptureResult --> ValidateAssertion: Verify Expected Outcome
    ValidateAssertion --> TestResult: Pass/Fail
    
    LogError --> TestResult
    TestResult --> Screenshot: Capture Screenshot
    Screenshot --> [*]
    
    style Initialize fill:#4caf50,color:#fff
    style Interact fill:#2196f3,color:#fff
    style Screenshot fill:#ff9800,color:#fff
    style LogError fill:#f44336,color:#fff
    style TestResult fill:#ffc107,color:#000
```

---

## 11. Complete Test Execution Cycle

```mermaid
graph TB
    subgraph Setup["SETUP PHASE"]
        S1["1. Load Configurations"]
        S2["2. Initialize WebDriver"]
        S3["3. Launch Application"]
    end
    
    subgraph Execution["EXECUTION PHASE"]
        E1["4. Execute Test 1: Open Website"]
        E2["5. Execute Test 2: Verify Page One"]
        E3["6. Execute Test 3: Verify Dropdown"]
        E4["7. Execute Test 4: Multiple Selection"]
        E5["8. Execute Test 5: Dropdown Options"]
        E6["9. Execute Test 6: Text Area Input"]
    end
    
    subgraph Validation["VALIDATION PHASE"]
        V1["10. Compare Expected vs Actual"]
        V2["11. Log Results"]
        V3["12. Capture Screenshots"]
    end
    
    subgraph Reporting["REPORTING PHASE"]
        R1["13. Generate Test Report"]
        R2["14. Generate HTML Report"]
        R3["15. Archive Logs & Screenshots"]
    end
    
    subgraph Cleanup["CLEANUP PHASE"]
        C1["16. Close Browser"]
        C2["17. Release Resources"]
        C3["18. Exit"]
    end
    
    S1 --> S2 --> S3
    S3 --> E1 --> E2 --> E3 --> E4 --> E5 --> E6
    E6 --> V1 --> V2 --> V3
    V3 --> R1 --> R2 --> R3
    R3 --> C1 --> C2 --> C3
    
    style Setup fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Execution fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    style Validation fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Reporting fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style Cleanup fill:#ffebee,stroke:#b71c1c,stroke-width:2px
```

---

## 12. Error Handling & Logging Flow

```mermaid
graph TD
    Test["Test Execution"] --> CheckPass{Assertion<br/>Passes?}
    CheckPass -->|Yes| LogPass["✅ logger.info()"]
    CheckPass -->|No| CatchError["⚠️ Exception Caught"]
    
    LogPass --> Screenshot1["📸 Save Screenshot<br/>Success"]
    CatchError --> LogError["❌ logger.error()"]
    LogError --> Screenshot2["📸 Save Screenshot<br/>Failure"]
    
    Screenshot1 --> Pass["PASS"]
    Screenshot2 --> Fail["FAIL"]
    
    Pass --> Report["Generate Report"]
    Fail --> Report
    Report --> Archive["Archive in /logs<br/>& /screenshot"]
    Archive --> End["Test Complete"]
    
    style Test fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style CheckPass fill:#ffc107,stroke:#f57f17,stroke-width:2px
    style LogPass fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style LogError fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
    style Pass fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style Fail fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
```

---

## 13. Locator Resolution Flow

```mermaid
graph LR
    Start["🎯 Element Locator"] --> Type{Locator<br/>Type?}
    Type -->|XPath| XPath["Use XPath Expression<br/>(By.XPATH)"]
    Type -->|CSS| CSS["Use CSS Selector<br/>(By.CSS_SELECTOR)"]
    Type -->|ID| ID["Use Element ID<br/>(By.ID)"]
    
    XPath --> Validate["Validate Locator"]
    CSS --> Validate
    ID --> Validate
    
    Validate --> Search["Search in DOM"]
    Search --> Found{Element<br/>Found?}
    Found -->|Yes| Return["Return WebElement"]
    Found -->|No| Retry["Retry/Timeout"]
    Retry --> Error["❌ NoSuchElementException"]
    
    Return --> Use["Use Element<br/>for Interaction"]
    Use --> End["✅ Complete"]
    
    style Start fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style XPath fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Found fill:#ffc107,stroke:#f57f17,stroke-width:2px
    style Return fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
    style Error fill:#f44336,stroke:#b71c1c,color:#fff,stroke-width:2px
    style End fill:#4caf50,stroke:#1b5e20,color:#fff,stroke-width:2px
```

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🚀 | Start/Launch |
| ✅ | Success/Pass |
| ❌ | Failure/Error |
| 📝 | Logging |
| 🖼️ | Screenshot |
| 🎯 | Locator/Target |
| ⚙️ | Configuration |
| 🌐 | Web Browser |
| ⏱️ | Wait/Delay |
| 📋 | Dropdown/Select |

---

## Summary

This documentation covers:

1. **Project Architecture** - Overall structure and dependencies
2. **Test Execution Flow** - How tests are run end-to-end
3. **Driver Initialization** - Browser setup and teardown
4. **Individual Test Flows** - Each test's execution path
5. **Element Interactions** - How elements are located and used
6. **Error Handling** - Logging and failure scenarios
7. **Locator Resolution** - How elements are found in the DOM

All flows use color-coded Mermaid diagrams for easy visualization and understanding.
