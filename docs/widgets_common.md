# WebSe_*-Widget-Klassenreferenz (Selenium)

Treiberspezifische Widget-Implementierungen fuer Selenium WebDriver.

> Fuer das generische Vererbungskonzept, die Erweiterungsstrategie (Unternehmens-
> / Projekt- / Einzelanpassung) und das OkwWidget-Interface siehe:
> [okw4robot/docs/widgets_common.md](http://192.168.1.130:3000/Hrabovszki1023/robotframework-okw4robot/src/branch/main/docs/widgets_common.md)

---

## WebSe_Base (Selenium-Basis)

Pfad: `okw_web_selenium/widgets/webse_base.py`

Erbt von `OkwWidget`. Implementiert die allgemeine Selenium-Logik fuer den
HTML-Standard:

- **Interaktion**: `okw_click()`, `okw_double_click()`, `okw_move_over()`, `okw_delete()`
- **Zustand**: `okw_exists()`, `okw_is_visible()`, `okw_is_enabled()`, `okw_is_editable()`,
  `okw_has_focus()`, `okw_is_focusable()`, `okw_is_clickable()`, `okw_set_focus()`
- **Werte lesen**: `okw_get_text()`, `okw_get_label()`, `okw_get_tooltip()`,
  `okw_get_placeholder()`, `okw_get_attribute(name)`
- **Sync**: `_wait_before(intent)` – exists → scroll → visible → enabled → editable → busy

Alle konkreten WebSe_*-Widgets erben von dieser Klasse und ueberschreiben nur
die Methoden, die widgetspezifisch sind (z.B. `okw_set_value`, `okw_get_value`).

---

## WebSe_Button

Pfad: `okw_web_selenium/widgets/webse_button.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_get_value()` | Sichtbarer Text (`innerText`) als Wert |

---

## WebSe_TextField

Pfad: `okw_web_selenium/widgets/webse_textfield.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_set_value(value)` | `clear()` + `input_text()` |
| `okw_get_value()` | `adapter.get_value()` (Attribut `value`) |
| `okw_type_key(key)` | `press_keys()` |

---

## WebSe_MultilineField

Pfad: `okw_web_selenium/widgets/webse_multilinefield.py`

Erbt von `WebSe_TextField`. Identisches Verhalten (fuer `<textarea>`).

---

## WebSe_Label

Pfad: `okw_web_selenium/widgets/webse_label.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_get_value()` | `adapter.get_text()` (sichtbarer Text) |

---

## WebSe_CheckBox

Pfad: `okw_web_selenium/widgets/webse_checkbox.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_set_value(value)` | Akzeptiert `Checked`/`Unchecked`/`True`/`False`/`Yes`/`No` |
| `okw_get_value()` | `"Checked"` oder `"Unchecked"` |

```robotframework
SetValue     AGB akzeptiert    Checked
VerifyValue  AGB akzeptiert    Checked
SetValue     AGB akzeptiert    Unchecked
```

---

## WebSe_ComboBox

Pfad: `okw_web_selenium/widgets/webse_combobox.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_set_value(value)` | Editable: clear+type. Non-editable: `select_by_label` |
| `okw_select(value)` | `select_by_label()` |
| `okw_get_value()` | Aktuell ausgewaehlter Wert |
| `okw_type_key(key)` | `press_keys()` (nur wenn editable) |

Fuer Details: [widgets_combobox_listbox.md](widgets_combobox_listbox.md)

---

## WebSe_RadioList

Pfad: `okw_web_selenium/widgets/webse_radiolist.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_select(value)` | Waehlt Radio-Button per `value` innerhalb der Gruppe |
| `okw_get_value()` | Aktuell ausgewaehlter Wert |

YAML-Varianten:
- Name-basiert: `group: zahlungsmethode`
- Container-basiert: `locator: { css: '[data-testid="..."]' }`

Fuer Details: [radiolist.md](radiolist.md)

---

## WebSe_ListBox

Pfad: `okw_web_selenium/widgets/webse_listbox.py`

| Methode | Verhalten |
|---------|-----------|
| `okw_select(value)` / `okw_set_value(value)` | Auswahl per Label |
| `okw_get_value()` | Kommaseparierte Liste der ausgewaehlten Werte |

Fuer Details: [widgets_combobox_listbox.md](widgets_combobox_listbox.md)

---

## WebSe_Table

Pfad: `okw_web_selenium/widgets/webse_table.py`

| Methode | Verhalten |
|---------|-----------|
| `get_cell_text(row, col)` | Text einer Zelle (0-basiert) |
| `get_row_texts(row)` | Alle Zellenwerte einer Zeile |
| `get_column_texts(col)` | Alle Zellenwerte einer Spalte |
| `get_row_count()` | Anzahl `<tr>` in `<tbody>` |
| `get_column_count()` | Anzahl `<th>` in `<thead>` |
| `get_header_names()` | Spaltennamen aus `<thead>` |

---

## YAML-Beispiel

**„Ein Fenster ist das, was man als Fenster definiert."** Fenster haben —
wie jedes Widget — eine eigene `class` und einen `locator`. Siehe
okw4robot CONTRACT.md (Abschnitt „Window-Modell") fuer das vollstaendige Konzept.

```yaml
# locators/MyApp.yaml
MyApp:
  __self__:
    class: okw_web_selenium.adapters.selenium_web.SeleniumWebAdapter
    browser: chrome
    url: https://example.com

  # Fenster: ein logischer GUI-Bereich mit eigener class + locator
  LoginDialog:
    class: okw_web_selenium.widgets.webse_panel.WebSe_Panel
    locator: { css: '[data-testid="login-page"]' }

    Benutzer:
      class: okw_web_selenium.widgets.webse_textfield.WebSe_TextField
      locator: { css: '[data-testid="username"]' }

    Passwort:
      class: okw_web_selenium.widgets.webse_textfield.WebSe_TextField
      locator: { css: '[data-testid="password"]' }

    OK:
      class: okw_web_selenium.widgets.webse_button.WebSe_Button
      locator: { css: '[data-testid="login"]' }

    Status:
      class: okw_web_selenium.widgets.webse_label.WebSe_Label
      locator: { css: '[data-testid="status-text"]' }

  # Logisches "Fenster" — eine Sidebar (immer sichtbar)
  NavBar:
    class: okw_web_selenium.widgets.webse_panel.WebSe_Panel
    locator: { css: "nav#main-nav" }

    btnHome:
      class: okw_web_selenium.widgets.webse_button.WebSe_Button
      locator: { css: "a[href='/']" }
```

```robot
*** Test Cases ***
Login Test
    StartApp        MyApp
    SelectWindow    LoginDialog
    SetValue        Benutzer    admin
    SetValue        Passwort    secret
    ClickOn         OK

    SelectWindow    NavBar
    ClickOn         btnHome
```
