# OKW Web Selenium

Selenium WebDriver plugin for [OKW4Robot](https://github.com/Hrabovszki1023/robotframework-okw4robot) —
the driver-agnostic keyword library for [Robot Framework](https://robotframework.org/).

This package provides `WebSe_*` widget implementations that translate
OKW keywords (`SetValue`, `ClickOn`, `VerifyValue`, ...) into Selenium
WebDriver calls for Chrome, Firefox, Edge and other browsers.

> **Deutsche Version:** [README_de.md](README_de.md)

---

## Installation

```bash
pip install robotframework-okw-web-selenium
```

This automatically installs `robotframework-okw4robot` (core) and
`robotframework-seleniumlibrary` as dependencies.

---

## Quick Start

```robotframework
*** Settings ***
Library    okw_web_selenium.library.OkwWebSeleniumLibrary

*** Test Cases ***
Login Test
    StartHost     Chrome
    StartApp      Chrome
    SelectWindow  Chrome
    SetValue      URL              https://example.com/login
    StartApp      MyApp
    SelectWindow  LoginDialog
    SetValue      Username         admin
    SetValue      Password         secret
    ClickOn       Login
    VerifyValue   Status           Logged in
    StopHost
```

All keywords come from the core (`okw4robot`). This package only provides
the Selenium-specific widget implementations — you never import individual
keyword modules.

---

## How It Works

```
OKW4Robot keyword              This package (WebSe_*)
─────────────────              ──────────────────────
SetValue "Name" "Smith"   →   WebSe_TextField.okw_set_value("Smith")
                               └→ Selenium: clear + input_text

ClickOn "Login"           →   WebSe_Button.okw_click()
                               └→ Selenium: click_element

VerifyValue "Status" "OK" →   WebSe_Label.okw_get_value()
                               └→ Selenium: get_text → polling loop
```

The YAML locator file determines which `WebSe_*` class is used for each
GUI object:

```yaml
# locators/MyApp.yaml
MyApp:
  LoginDialog:
    Username:
      class: okw_web_selenium.widgets.webse_textfield.WebSe_TextField
      locator: { id: user_input }
    Password:
      class: okw_web_selenium.widgets.webse_textfield.WebSe_TextField
      locator: { id: password_input }
    Login:
      class: okw_web_selenium.widgets.webse_button.WebSe_Button
      locator: { css: "button[type=submit]" }
```

---

## Widget Classes

| Class | HTML Elements | Key Methods |
|-------|--------------|-------------|
| `WebSe_TextField` | `<input>`, `<textarea>` | set_value, type_key, get_value, delete |
| `WebSe_Button` | `<button>`, `<input type=button>` | click, double_click, get_text |
| `WebSe_CheckBox` | `<input type=checkbox>` | click, set_value, get_value |
| `WebSe_ComboBox` | `<select>`, custom dropdowns | select, get_value, get_list_count |
| `WebSe_ListBox` | `<select multiple>`, `<ul>` lists | select, get_value, get_list_count |
| `WebSe_RadioList` | `<input type=radio>` groups | select, get_value |
| `WebSe_Label` | `<span>`, `<div>`, `<p>`, `<label>` | get_value, get_text |
| `WebSe_Link` | `<a>` | click, get_text |
| `WebSe_Table` | `<table>` | get_cell_value, get_row_count, get_headers |
| `WebSe_MultilineField` | `<textarea>`, contenteditable | set_value, type_key, get_value |
| `BrowserControl` | Browser host | start, stop, select_window |
| `UrlBar` | Address bar | set_value (navigate to URL) |

Full reference: [docs/widgets_common.md](docs/widgets_common.md)

---

## Documentation

- [docs/README.md](docs/README.md) – Documentation overview
- [docs/widgets_common.md](docs/widgets_common.md) – WebSe_* class reference
- [docs/Web_Widget_Matrix.md](docs/Web_Widget_Matrix.md) – HTML element → widget mapping
- [docs/radiolist.md](docs/radiolist.md) – RadioList locator strategies
- [docs/docs_host_app_config.md](docs/docs_host_app_config.md) – Host/App YAML configuration
- [docs/executejs-snippets.md](docs/executejs-snippets.md) – JavaScript snippets for ExecuteJS

For core documentation (keywords, contracts, timeouts, sync strategy) see
[robotframework-okw4robot](https://github.com/Hrabovszki1023/robotframework-okw4robot).

---

## Project Structure

```
robotframework-okw-web-selenium/
  src/okw_web_selenium/
    library.py              # OkwWebSeleniumLibrary (extends OKW4RobotLibrary)
    adapter.py              # SeleniumAdapter (browser lifecycle)
    widgets/
      webse_base.py         # WebSe_Base (shared Selenium logic)
      webse_textfield.py    # WebSe_TextField
      webse_button.py       # WebSe_Button
      webse_checkbox.py     # WebSe_CheckBox
      webse_combobox.py     # WebSe_ComboBox
      webse_listbox.py      # WebSe_ListBox
      webse_radiolist.py    # WebSe_RadioList
      webse_label.py        # WebSe_Label
      webse_link.py         # WebSe_Link
      webse_table.py        # WebSe_Table
      webse_multilinefield.py
      host/
        browsercontrol/     # BrowserControl + UrlBar
    locators/               # Built-in YAML locators (Chrome, WidgetsDemo, ...)
  tests/
    robot/                  # 53 Robot Framework integration tests
  docs/
```

---

## License

- **Community** (non-commercial): see [LICENSE](LICENSE)
- **Commercial**: see [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md)
- **FAQ**: [docs/license_faq.md](docs/license_faq.md)
