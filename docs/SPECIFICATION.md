# OKW Web Selenium – SPECIFICATION

Diese Spezifikation beschreibt die **Semantik** der OKW-Web-Keywords für die Selenium-Implementierung.
Sie ist bewusst **technik-neutral** formuliert (Selenium ist Implementierungsdetail), aber auf **Web-Widgets** bezogen.

---

## 1. Grundprinzipien

- **Abstrakte Widget-Namen**: Alle Keywords adressieren Widgets über einen abstrakten Namen (`<Name>`), der im Modell (YAML) auf konkrete Lokatoren aufgelöst wird.
- **Determinismus**: Verify-Keywords sind *wartend* (Polling) und liefern bei Nichterfüllung innerhalb des Timeouts einen eindeutigen Fehler.
- **Keine Technik im Keyword**: Keyword-Namen enthalten keine Technik (kein „Selenium“ im Keyword).

---

## 2. Matching-Modi

Viele Verify-Keywords existieren in drei Varianten:

- **Exact** (ohne Suffix): exakter Stringvergleich.
- **WCM**: Wildcard Matching  
  - `*` = beliebige Zeichenfolge  
  - `?` = genau ein Zeichen
- **REGX**: Regular Expressions

Hinweis: In Robot Framework müssen Backslashes in Strings ggf. doppelt escaped werden (z. B. `^A3\\d$` → in Robot oft `^A3\\\\d$`).

---

## 3. Warten, Polling, Timeouts

Verify-Keywords verwenden Polling bis zum Sollzustand oder Timeout.

### Polling
- Intervall: `${OKW_POLL_VERIFY}` (Default typischerweise 0.1s)

### Timeouts (aus `okw_parameters.md`)
- Value:
  - `${OKW_TIMEOUT_VERIFY_VALUE}` (Default 10s)
- Placeholder:
  - `${OKW_TIMEOUT_VERIFY_PLACEHOLDER}` (Default 10s)
- Tooltip:
  - `${OKW_TIMEOUT_VERIFY_TOOLTIP}` (Default 10s)
- Table:
  - `${OKW_TIMEOUT_VERIFY_TABLE}` (Default z. B. 2s)
- List:
  - `${OKW_TIMEOUT_VERIFY_LIST}` (Default z. B. 2s)

> Die konkreten Defaults können per Robot-Variablen überschrieben werden.

---

## 4. Ignore-Regeln / No-Op

Globales Ignorieren leerer Eingaben/Erwartungen:

- `${OKW_IGNORE_EMPTY}`: wenn aktiv, können bestimmte Keywords bei leeren Sollwerten zu einem No-Op werden (z. B. „nichts zu prüfen“).
- Weitere Ignore-Regeln sind in `keywords_ignore_rule.md` beschrieben.

Ziel: Konfigurierbar bleiben, ohne Testfälle mit Kontrolllogik zu überladen.

---

## 5. Widget-Semantik

### Value vs. Label vs. Caption vs. Tooltip

- **Value**: Inhalt/Wert des Widgets (z. B. Input-Value, Checkbox-State, Selection).
- **Label**: *Beschriftung* eines Controls (z. B. über `aria-labelledby`, `<label for=…>`, `aria-label`, Fallback-Text).
- **Caption**: sichtbarer Text des Elements selbst (z. B. Button-Text, Link-Text, Label-Text).
- **Tooltip**: Tooltip-Text, typischerweise aus `title`, Fallback `aria-label`.
- **Placeholder**: Placeholder-Text, typischerweise aus `placeholder` (bei nativen `<select>` oft leer).

---

## 6. Tabellen (Web)

Tabellen-Keywords arbeiten mit einer Text-Repräsentation der Tabelle.

### Indizierung
- `row`/`col` sind **1-basiert**.
- Header kann über `row=0` adressiert werden (Header-Zellen).

### Tokens (Standard)
- `$TAB` trennt Zellen
- `$LF` trennt Zeilen
- `$EMPTY` = leere Zelle
- `$EMPTYCOL` = leere Spalte
- `$EMPTYTABLE` = leere Tabelle

Literal-Tokens können mit Backslash escaped werden (z. B. `\$TAB`).

### Header-basierte Zugriffe
- Zeile wird über einen **RowKey** (WCM) identifiziert.
- Spalte über **exakten Header-Text**.

### Regex-Varianten
- Für per-Zelle Regex Matching; `$EMPTY` steht für leere Zelle.

---

## 7. Listen (Web)

Listen-Keywords zählen Einträge bzw. ausgewählte Einträge:

- `VerifyListCount` zählt Einträge (ListBox, RadioList, native `<select>`)
- `VerifySelectedCount` zählt ausgewählte Einträge (RadioList meist 0/1)

Auch hier: wartend bis Timeout.

---

## 8. Kontext (Host / App / Window)

Kontext-Keywords steuern den aktiven Host, die App und das Fenster.
Die Zustandsverwaltung ist in `context.md` und `keywords_host_app*.md` beschrieben.

---

## 9. Fehlerverhalten (Normativ)

- Verify-Keywords schlagen fehl, wenn der Sollzustand **innerhalb des Timeouts** nicht erreicht wird.
- Fehler sollen den Widget-Namen, die erwarteten Werte/Pattern und den zuletzt beobachteten Ist-Wert enthalten (Debugbarkeit).
