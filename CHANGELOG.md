# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2026-02-22

### Highlights
- Fully functional end-to-end: 53/53 Robot Framework tests PASS
- Separated from okw4robot as independent driver package
- English README (PyPI-ready), cleaned documentation

### Features
- `OkwWebSeleniumLibrary` as single library import (inherits all okw4robot keywords)
- `super().__init__()` fix in library, BrowserControl, UrlBar
- `locators/__init__.py` created for `importlib.resources` compatibility
- `robotframework-seleniumlibrary>=6.0` added as dependency
- `pyproject.toml`: package-data for YAML locator files

### Tests
- All 24 Robot test files updated: single library import, corrected StartApp paths, removed keyword prefixes (KW., PH., TBL., etc.)
- 4 obsolete test files removed (swingtest, demo, Login_alt)
- 53/53 Robot Framework integration tests PASS

### Docs
- `README.md`: English version (PyPI-ready); `README_de.md` for German
- `docs/widgets_common.md`: WebSe_* class reference (all widget classes documented)
- `docs/README.md`: Updated to reflect cleaned documentation structure
- 22 generic docs removed (belong in okw4robot)
- 3 prompt duplicates removed
- Terminology: "treiberunabhaengig" → "treiberagnostisch"

### Breaking Changes
- Single library import: `Library okw_web_selenium.library.OkwWebSeleniumLibrary` replaces all previous multi-import patterns
- Robot test files must use unprefixed keyword names (e.g. `SetValue` not `KW.SetValue`)

## [0.2.0] - 2025-10-19

### Highlights
- Initial Selenium adapter separation from okw4robot
- WebSe_* widget classes for all standard HTML elements
- YAML locator system for GUI object mapping

### Features
- WebSe_TextField, WebSe_Button, WebSe_CheckBox, WebSe_ComboBox, WebSe_ListBox, WebSe_RadioList, WebSe_Label, WebSe_Link, WebSe_Table, WebSe_MultilineField
- BrowserControl + UrlBar for browser host management
- SeleniumAdapter for browser lifecycle (open, close, switch window)
- YAML locator files for Chrome, WidgetsDemo, TableDemo test apps

### Compatibility
- Python: >= 3.10
- robotframework: >= 6.0
- robotframework-okw4robot: >= 0.4.0
- selenium: >= 4.0

[0.3.0]: https://github.com/Hrabovszki1023/robotframework-okw-web-selenium/releases/tag/v0.3.0
[0.2.0]: https://github.com/Hrabovszki1023/robotframework-okw-web-selenium/releases/tag/v0.2.0
