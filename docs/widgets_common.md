# Common Widgets (Web)

Diese Seite dokumentiert die treiberâ€‘agnostischen Commonâ€‘Widgets und deren Methoden. Commonâ€‘Widgets kapseln die generische Interaktionslogik; die eigentliche AusfÃ¼hrung erfolgt Ã¼ber den aktiven Adapter (z.â€¯B. Selenium).

---

## Grundlagen

- Adapterâ€‘Schnittstelle: Widgets rufen ausschlieÃŸlich Methoden am Adapter auf (z.â€¯B. `click`, `get_text`, `get_value`, `wait_until_visible`). Alle Webâ€‘Adapter mÃ¼ssen diese Methoden im gleichen Sinne bereitstellen.
- Locatorâ€‘Format: YAMLâ€‘Locatoren sind in der Regel ein Dict mit genau einem SchlÃ¼ssel, z.â€¯B. `{ css: '...' }`, `{ xpath: '...' }`. Die AuflÃ¶sung Ã¼bernimmt der Adapter.
- Fehlersemantik:
  - UngÃ¼ltige Locatorâ€‘Formate â†’ `ValueError` (Adapter)
  - Nicht gefundene Elemente bei Verifikationen â†’ `AssertionError`
  - Laufzeitfehler des Backends â†’ `RuntimeError` (Adapter) oder spezifische Exceptions

---

## KlassenÃ¼bersicht

### BaseWidget
Abstrakte Basisklasse, von der alle Widgets erben.

- Konstruktor: `BaseWidget(adapter, locator)`
- Gemeinsame Felder:
  - `self.adapter`: aktiver Adapter (z.â€¯B. Selenium)
  - `self.locator`: YAMLâ€‘Locator (Dict oder String)
- Methoden (Contract; Default teils `NotImplemented`):
  - `okw_click()` â†’ Klickt auf das Element.
  - `okw_double_click()` â†’ Doppelklick auf das Element.
  - `okw_set_value(value)` â†’ Setzt einen Wert (z.â€¯B. Eingabefeld).
  - `okw_select(value)` â†’ Auswahl (z.â€¯B. Dropdown) per Label/Value/Index.
  - `okw_type_key(key)` â†’ Sendet Tasten an das Element.
  - `okw_verify_value(expected)` â†’ PrÃ¼ft exakte Gleichheit; `AssertionError` bei Abweichung.
  - `okw_verify_value_wcm(expected)` â†’ Wildcardâ€‘Match (`*`/`?`), `AssertionError` bei Missmatch.
  - `okw_verify_value_regex(expected)` â†’ Regexâ€‘Match, `AssertionError` bei Missmatch.
  - `okw_verify_exist()` â†’ Gibt `True/False` zurÃ¼ck, ob Element existiert (implementiert in BaseWidget via Adapter).
  - `okw_log_value()` â†’ Loggt den aktuellen Wert/Text.
  - `okw_has_value()` â†’ Gibt an, ob ein inhaltlicher Wert vorhanden ist (Widgetâ€‘spezifisch; ggf. nicht implementiert).
  - `okw_memorize_value()` â†’ Liefert den aktuellen Wert/Text zurÃ¼ck (fÃ¼r Variablenablage).

Hinweis: `okw_verify_exist()` ist in `BaseWidget` bereits implementiert und nutzt `adapter.element_exists(locator)`.

---

### Button
Pfad: `src/okw4robot/widgets/common/button.py`

- Implementiert:
  - `okw_click()` â†’ `adapter.click(locator)`
  - `okw_double_click()` â†’ `adapter.double_click(locator)`
- Typische Adapterâ€‘Methoden: `click`, `double_click`

Projektanpassung: Ãœber Vererbung (z.â€¯B. `MyProjectButton`) kÃ¶nnen zusÃ¤tzliche Wartebedingungen implementiert werden, bevor geklickt wird.

---

### TextField
Pfad: `src/okw4robot/widgets/common/text_field.py`

- Implementiert:
  - `okw_set_value(value)` â†’ Clear+Type: optional `adapter.clear_text(locator)`, dann `adapter.input_text(locator, value)`
  - `okw_click()` â†’ `adapter.click(locator)`
  - `okw_verify_value(expected)` â†’ liest `adapter.get_value(locator)` und vergleicht exakt
  - `okw_verify_value_wcm(expected)` â†’ Wildcardâ€‘Vergleich (`*`, `?`) auf dem Feldwert
  - `okw_verify_value_regex(expected)` â†’ Regexâ€‘Vergleich auf dem Feldwert
  - `okw_log_value()` â†’ loggt `adapter.get_value(locator)`
  - `okw_memorize_value()` â†’ gibt `adapter.get_value(locator)` zurÃ¼ck
- Typische Adapterâ€‘Methoden: `input_text`, `clear_text`, `get_value`, `click`

Hinweis: Es existiert zusÃ¤tzlich eine Hilfsmethode `okw_exists()` (nur in diesem Widget); fÃ¼r Keywordâ€‘PrÃ¼fungen wird jedoch `okw_verify_exist()` aus `BaseWidget` verwendet.

---

### Label
Pfad: `src/okw4robot/widgets/common/label.py`

- Implementiert:
  - `okw_verify_value(expected)` â†’ liest `adapter.get_text(locator)` und vergleicht exakt
  - `okw_verify_value_wcm(expected)` â†’ Wildcardâ€‘Vergleich (`*`, `?`) auf dem Text
  - `okw_verify_value_regex(expected)` â†’ Regexâ€‘Vergleich auf dem Text
  - `okw_log_value()` â†’ loggt `adapter.get_text(locator)`
  - `okw_memorize_value()` â†’ gibt `adapter.get_text(locator)` zurÃ¼ck
- Typische Adapterâ€‘Methoden: `get_text`

---

### CheckBox
Pfad: `src/okw4robot/widgets/common/checkbox.py`

- Konzept: Zustandsbasiertes Setzen; `SetValue` hinterlÃ¤sst die Checkbox im gewÃ¼nschten Zustand, ohne blind zu toggeln.
- Implementiert:
  - `okw_set_value(value)` â€“ akzeptiert `Checked`/`Unchecked` sowie Synonyme (`True/Yes/1` bzw. `False/No/0`); nutzt `adapter.set_checkbox(locator, checked)`, das nur klickt, wenn eine ZustandsÃ¤nderung nÃ¶tig ist.
  - `okw_verify_value(expected)` â€“ erwartet `Checked` oder `Unchecked` und prÃ¼ft via `adapter.is_checkbox_selected`.
  - `okw_click()` â€“ toggelt den Zustand; fÃ¼r definierte EndzustÃ¤nde `SetValue` bevorzugen.
  - `okw_log_value()` / `okw_memorize_value()` â€“ geben `"Checked"`/`"Unchecked"` aus bzw. zurÃ¼ck.
- Typische Adapter-Methoden: `set_checkbox`, `is_checkbox_selected`.

Robot-Beispiele:
```robotframework
SetValue     myCheckbox    Checked
VerifyValue  myCheckbox    Checked
SetValue     myCheckbox    Unchecked
VerifyValue  myCheckbox    Unchecked
```

---

### RadioList
Pfad: `src/okw4robot/widgets/common/radiolist.py`

- Konzept:
  - Gruppe (`group`) entspricht dem HTML-`name` Attribut der Radios.
  - Auswahlwert ist der HTML-`value` des gewÃ¼nschten Radio-Buttons (nicht automatisch der sichtbare Label-Text).
- Implementiert:
  - `okw_select(value)` â†’ wÃ¤hlt per `value` innerhalb der `group`.
  - `okw_verify_value(expected)` â†’ prÃ¼ft, dass die `group` auf `expected` gesetzt ist.

HTML-Beispiel:
```html
<form>
  <fieldset>
    <legend>Zahlungsart</legend>
    <label>
      <input type="radio" name="paymentMethod" value="paypal">
      PayPal
    </label>
    <label>
      <input type="radio" name="paymentMethod" value="visa">
      Visa (Kreditkarte)
    </label>
    <label>
      <input type="radio" name="paymentMethod" value="sepa">
      SEPA-Lastschrift
    </label>
  </fieldset>
  <!-- Sichtbarer Text (PayPal, Visa, SEPA) kann vom value abweichen -->
  <!-- GewÃ¤hlt wird standardmÃ¤ÃŸig per value-Attribut (paypal/visa/sepa). -->
  </form>
```

YAML-Beispiel:
```yaml
PaymentMethod:
  class: okw4robot.widgets.common.radiolist.RadioList
  group: paymentMethod   # HTML name-Attribut
```

Robot-Beispiel:
```robotframework
Select        PaymentMethod    paypal
VerifyValue   PaymentMethod    paypal
```

Hinweis: Falls Auswahl per sichtbarem Text gewÃ¼nscht ist, kann ein Labelâ†’Value-Mapping als YAML-Extras ergÃ¤nzt und im Widget ausgewertet werden (optional erweiterbar).

---

## Robotâ€‘Keywords â†’ Widgetâ€‘Methoden (Mapping)
Die Bibliothek `WidgetKeywords` ruft je nach Keyword die passende Widgetâ€‘Methode auf:

- `ClickOn    <Name>` â†’ `okw_click()`
- `DoubleClickOn    <Name>` â†’ `okw_double_click()`
- `SetValue    <Name>    <Wert>` â†’ `okw_set_value(value)`
- `Select    <Name>    <Wert>` â†’ `okw_select(value)`
- `TypeKey    <Name>    <Key>` â†’ `okw_type_key(key)`
- `VerifyValue    <Name>    <Soll>` â†’ `okw_verify_value(expected)`
- `VerifyValueWCM    <Name>    <Soll>` â†’ `okw_verify_value_wcm(expected)`
- `VerifyValueREGX   <Name>    <Regex>` â†’ `okw_verify_value_regex(expected)`
- `VerifyExist    <Name>    YES|NO` â†’ nutzt `okw_verify_exist()` und prÃ¼ft gegen Erwartung
- `LogValue    <Name>` â†’ `okw_log_value()`
- `HasValue    <Name>` â†’ `okw_has_value()` (falls implementiert)
- `MemorizeValue    <Name>    <Variable>` â†’ `okw_memorize_value()`

Pfad: `src/okw4robot/keywords/widget_keywords.py`

Siehe auch: `docs/keywords_ignore_rule.md` (Ignore-Regel, $IGNORE; optional ${OKW_IGNORE_EMPTY}; $DELETE bei TypeKey).

---

## YAMLâ€‘Beispiel

```yaml
LoginDialog:
  __self__:
    class: okw4robot.widgets.common.label.Label
    locator: { css: '[data-testid="login-page"]' }

  Benutzer:
    class: okw4robot.widgets.common.text_field.TextField
    locator: { css: '[data-testid="username"]' }

  Passwort:
    class: okw4robot.widgets.common.text_field.TextField
    locator: { css: '[data-testid="password"]' }

  OK:
    class: okw4robot.widgets.common.button.Button
    locator: { css: '[data-testid="login"]' }

  Status:
    class: okw4robot.widgets.common.label.Label
    locator: { css: '[data-testid="status-text"]' }
```

---

## Projektspezifische Erweiterungen

- Vererbung: Ableiten von Commonâ€‘Widgets, um projektartige Besonderheiten (z.â€¯B. Busyâ€‘Overlayâ€‘Warte) zu kapseln.
  - Beispiel: `src/okw4robot/widgets/myproject/button.py` wartet vor dem Klick, bis eine Progressbar nicht sichtbar ist, und ruft dann `super().okw_click()`.
- YAMLâ€‘Umschaltung: Widgets, die das Verhalten benÃ¶tigen, verwenden die Projektklasse:
  - `class: okw4robot.widgets.myproject.button.MyProjectButton`
- Optional: Konfiguration Ã¼ber YAMLâ€‘Zusatzfelder (kann Ã¼ber eine Erweiterung der Widgetâ€‘Konstruktion unterstÃ¼tzt werden), um z.â€¯B. Busyâ€‘Overlayâ€‘Locatoren ohne CodeÃ¤nderung zu steuern.

---

## Adapterâ€‘AbhÃ¤ngigkeiten (Web)

FÃ¼r volle FunktionalitÃ¤t sollten Webâ€‘Adapter mindestens Folgendes bereitstellen:

- `click`, `double_click`, `input_text`, `clear_text`, `get_text`, `get_value`
- `element_exists`, `wait_until_visible`, `wait_until_not_visible`
- `select_by_label`, `select_by_value`, `select_by_index`
- `press_keys`
- (Hostâ€‘Widgets) `go_to`, `maximize_window`

Beispielâ€‘Adapter: `src/okw4robot/adapters/selenium_web.py`

