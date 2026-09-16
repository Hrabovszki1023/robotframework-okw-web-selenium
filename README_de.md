# OKW Web Selenium

[![PyPI](https://img.shields.io/pypi/v/robotframework-okw-web-selenium)](https://pypi.org/project/robotframework-okw-web-selenium/)
[![Python](https://img.shields.io/pypi/pyversions/robotframework-okw-web-selenium)](https://pypi.org/project/robotframework-okw-web-selenium/)
[![License](https://img.shields.io/badge/License-OKW_Community-orange.svg)](LICENSE)

Selenium-WebDriver-Plugin für [OKW4Robot](https://github.com/Hrabovszki1023/robotframework-okw4robot) — die treiberunabhängige Keyword-Bibliothek für [Robot Framework](https://robotframework.org/).

> **English version:** [README.md](README.md)

## Signal vs. NOISE

| Signal (dein Test) | NOISE (versteckt in YAML + Widgets) |
|---|---|
| `SetValue Username admin` | `driver.find_element(By.ID, "user_input").clear(); .send_keys("admin")` |
| `ClickOn Login` | `WebDriverWait(...).until(EC.element_to_be_clickable(...)).click()` |
| `VerifyValue Status Logged in` | Polling-Schleife, Timeout, Element-Suche per CSS/XPath/ID |

---

## Installation

```bash
pip install robotframework-okw-web-selenium
```

Installiert automatisch `robotframework-okw4robot` (Core) und
`robotframework-seleniumlibrary` als Abhängigkeiten.

---

## Schnellstart

```robot
*** Settings ***
Library    okw_web_selenium.library.OkwWebSeleniumLibrary

*** Test Cases ***
Login Test
    StartApp      MyApp
    SelectWindow  LoginDialog
    SetValue      Username         admin
    SetValue      Password         secret
    ClickOn       Login
    VerifyValue   Status           Logged in
```

`StartApp` lädt die App-YAML (`locators/MyApp.yaml`). Enthält die YAML eine
`__self__`-Sektion mit Adapterklasse und Browser-Parameter, wird der Browser
automatisch geöffnet — kein separates `StartHost` nötig.

Alle Keywords kommen aus dem Core (`okw4robot`). Dieses Paket liefert nur
die Selenium-spezifischen Widget-Implementierungen — einzelne Keyword-Module
werden nie direkt importiert.

---

## So funktioniert es

```
OKW4Robot-Keyword              Dieses Paket (WebSe_*)
─────────────────              ──────────────────────
SetValue "Name" "Smith"   →   WebSe_TextField.okw_set_value("Smith")
                               └→ Selenium: clear + input_text

ClickOn "Login"           →   WebSe_Button.okw_click()
                               └→ Selenium: click_element

VerifyValue "Status" "OK" →   WebSe_Label.okw_get_value()
                               └→ Selenium: get_text → Polling-Schleife
```

Die YAML-Locator-Datei bestimmt, welche `WebSe_*`-Klasse für jedes
GUI-Objekt verwendet wird:

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

## iFrame-Unterstützung

Wenn ein Widget innerhalb eines `<iframe>` liegt, wird das `iframe`-Attribut
im YAML-Eintrag ergänzt. Der Adapter schaltet transparent in den Frame um,
bevor das Element angesprochen wird, und schaltet automatisch zurück, wenn
das nächste Widget außerhalb des Frames liegt.

```yaml
MyApp:
  PaymentPage:
    CardNumber:
      class: okw_web_selenium.widgets.webse_textfield.WebSe_TextField
      locator: { id: card-number }
      iframe: { css: "iframe#payment-frame" }
    Amount:
      class: okw_web_selenium.widgets.webse_label.WebSe_Label
      locator: { css: ".total-amount" }
```

Der Testcode bleibt unverändert — kein manuelles `switch_to.frame()`:

```robot
SetValue     CardNumber    4111111111111111
VerifyValue  Amount        €99.00
```

`CardNumber` liegt im iframe → der Adapter schaltet hinein.
`Amount` liegt außerhalb → der Adapter schaltet zurück zu `default_content`.

**Regeln:**
- `iframe` akzeptiert dieselben Locator-Strategien wie `locator` (css, xpath, id, ...).
- Verschachtelte iframes werden nicht unterstützt — nur eine Ebene tief.
- Der Wechsel wird pro Adapter verfolgt: Wenn zwei aufeinanderfolgende Widgets
  denselben iframe nutzen, wird nur einmal gewechselt.

---

## SetContext (Wiederholende Strukturen)

Webanwendungen enthalten häufig wiederholende Elemente — Produktkarten,
Tabellenzeilen, Listeneinträge — die intern dieselbe Struktur haben.
`SetContext` grenzt nachfolgende Widget-Operationen auf eine Instanz ein,
identifiziert durch einen Platzhalter-Wert. Jede Instanz muss nicht
einzeln im YAML definiert werden.

### YAML

```yaml
MyApp:
  Products:
    ProductCard:
      __context__:
        locator: { xpath: '//div[@class="product"][.//h3[text()="{ProductName}"]]' }
      Name:
        class: okw_web_selenium.widgets.webse_label.WebSe_Label
        locator: { xpath: './/h3' }
      Price:
        class: okw_web_selenium.widgets.webse_label.WebSe_Label
        locator: { xpath: './/span[@class="price"]' }
      AddToCart:
        class: okw_web_selenium.widgets.webse_button.WebSe_Button
        locator: { xpath: './/button[contains(@class,"add-to-cart")]' }
```

### Test

```robot
SelectWindow    Products
SetContext      ProductCard    Sauce Labs Backpack
VerifyValue     Price          $29.99
ClickOn         AddToCart

SetContext      ProductCard    Sauce Labs Bike Light
VerifyValue     Price          $9.99
ClickOn         AddToCart
```

**So funktioniert es:**

1. `SetContext ProductCard Sauce Labs Backpack` ersetzt `{ProductName}`
   im `__context__`-Locator.
2. Kind-Widgets nutzen relative Locatoren (`.//...`) — sie sind auf das
   gematchte Context-Element beschränkt.
3. `SelectWindow` löscht den Kontext automatisch.

**Regeln:**
- `__context__` ist ein reservierter Schlüssel — wie `__self__`.
- Platzhalter nutzen `{Name}`-Syntax, ersetzt über `str.format()`.
- Mehrere Platzhalter: `SetContext Tabellenzeile Zeile=A Spalte=3`.
- Context-Locatoren müssen **XPath** verwenden (CSS unterstützt keine
  Textauswahl und keine relative Pfadkomposition).
- Kind-Locatoren nutzen relatives XPath (`.//...`), beschränkt auf das
  Context-Element.

---

## Widget-Klassen

| Klasse | HTML-Elemente | Wichtige Methoden |
|--------|--------------|-------------------|
| `WebSe_TextField` | `<input>`, `<textarea>` | set_value, type_key, get_value, delete |
| `WebSe_Button` | `<button>`, `<input type=button>` | click, double_click, get_text |
| `WebSe_CheckBox` | `<input type=checkbox>` | click, set_value, get_value |
| `WebSe_ComboBox` | `<select>`, Custom-Dropdowns | select, get_value, get_list_count |
| `WebSe_ListBox` | `<select multiple>`, `<ul>`-Listen | select, get_value, get_list_count |
| `WebSe_RadioList` | `<input type=radio>`-Gruppen | select, get_value |
| `WebSe_Label` | `<span>`, `<div>`, `<p>`, `<label>` | get_value, get_text |
| `WebSe_Link` | `<a>` | click, get_text |
| `WebSe_Table` | `<table>` | get_cell_value, get_row_count, get_headers |
| `WebSe_MultilineField` | `<textarea>`, contenteditable | set_value, type_key, get_value |

Alle Widget-Klassen erben `click`, `move_over`, `get_tooltip`, `get_label`,
`get_attribute`, `get_placeholder` von `WebSe_Base`.

| `BrowserControl` | Browser-Host | start, stop, select_window |
| `UrlBar` | Adressleiste | set_value (URL aufrufen) |

Vollständige Referenz: [docs/widgets_common.md](docs/widgets_common.md)

---

## Web-spezifische Keywords

Diese Keywords sind nur mit `OkwWebSeleniumLibrary` verfügbar (nicht im
Core `OKW4RobotLibrary`):

| Keyword | Beschreibung |
|---------|--------------|
| `ExecuteJS` | Rohes JavaScript im Browser-Kontext ausführen |
| `RemoveAds` | Werbe-Iframes/Overlays per JS + MutationObserver entfernen |

### RemoveAds

Entfernt Werbeelemente von der aktuellen Seite. Ohne Argumente werden
gängige Google-Ads-Selektoren verwendet. Mit Argumenten wird jedes
Argument als CSS-Selektor für zu entfernende Elemente interpretiert.

Ein `MutationObserver` wird installiert, der Ads automatisch entfernt,
sobald sie asynchron nachgeladen werden. Ein Aufruf pro Seite genügt.

```robot
# Standard (Google Ads):
OnFailIgnoreNOISE    RemoveAds

# Projektspezifische Selektoren:
OnFailIgnoreNOISE    RemoveAds    div.custom-banner    iframe[src*="ad-network"]
```

Am besten mit `OnFailIgnoreNOISE` im Test-Setup verwenden — wenn die Seite
keine Ads hat, entfernt das Keyword einfach nichts und läuft weiter.

---

## Dokumentation

- [docs/README.md](docs/README.md) – Dokumentationsübersicht
- [docs/widgets_common.md](docs/widgets_common.md) – WebSe_*-Klassenreferenz
- [docs/Web_Widget_Matrix.md](docs/Web_Widget_Matrix.md) – HTML-Element → Widget-Zuordnung
- [docs/radiolist.md](docs/radiolist.md) – RadioList-Locator-Strategien
- [docs/docs_host_app_config.md](docs/docs_host_app_config.md) – Host/App-YAML-Konfiguration
- [docs/executejs-snippets.md](docs/executejs-snippets.md) – JavaScript-Snippets für ExecuteJS

Für Core-Dokumentation (Keywords, Contracts, Timeouts, Sync-Strategie) siehe
[robotframework-okw4robot](https://github.com/Hrabovszki1023/robotframework-okw4robot).

---

## Projektstruktur

```
robotframework-okw-web-selenium/
  src/okw_web_selenium/
    library.py              # OkwWebSeleniumLibrary (erweitert OKW4RobotLibrary)
    adapter.py              # SeleniumAdapter (Browser-Lebenszyklus)
    widgets/
      webse_base.py         # WebSe_Base (gemeinsame Selenium-Logik)
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
    locators/               # Eingebaute YAML-Locatoren (Chrome, WidgetsDemo, ...)
  tests/
    robot/                  # 53 Robot Framework Integrationstests
  docs/
```

---

## Lauffähige Beispiele

[okw-examples/selenium/](https://github.com/Hrabovszki1023/okw-examples/tree/main/selenium/) — Login, dynamische Tabelle, SetContext, Tokens.

## Handbuch

[OKW4Robot Handbuch](https://hrabovszki1023.github.io/okw-examples/) — Schritt-für-Schritt-Anleitung.

## KI-Testgenerierung

Testfälle können mit jeder KI (Claude, ChatGPT, Copilot, ...) generiert werden.
Die System-Prompts für die Testgenerierung werden zentral in
[`robotframework-okw4robot/prompts/`](https://github.com/Hrabovszki1023/robotframework-okw4robot/tree/main/prompts) gepflegt.

Kopieren Sie den Prompt in Ihre KI und beschreiben Sie in natürlicher Sprache, was Sie testen möchten.
Die KI erzeugt eine lauffähige `.robot`-Datei.

## Lizenz

- **Community** (nicht-kommerziell): siehe [LICENSE](LICENSE)
- **Kommerziell**: siehe [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md)
- **FAQ**: [docs/license_faq.md](docs/license_faq.md)
