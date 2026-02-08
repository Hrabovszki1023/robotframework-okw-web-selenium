## 1. Aktionen ohne Eingabewert
Kurzbeschreibung: Aktionen, die keine Werte übergeben bekommen (z. B. Klicks).

| Keyword       | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|---------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| ClickOn       |   ✓    |     ✓     |       ✓        |       |    ✓     |          |           |         |
| DoubleClickOn |   ✓    |           |                |       |          |          |           |         |
| SetFocus      |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |

## 2. Aktionen mit Eingabewert
Kurzbeschreibung: Aktionen, die einen Wert/Parameter benötigen (Eingaben, Auswahlen).

| Keyword  | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|----------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| SetValue |        |     ✓     |       ✓        |       |    ✓     |    ✓     |           |         |
| Select   |        |           |                |       |          |    ✓     |     ✓     |    ✓    |
| TypeKey  |        |     ✓     |       ✓        |       |          |    ✓     |           |         |

## 3. Verify (wartend, mit Timeout)
Kurzbeschreibung: Prüfungen, die bis zum Sollzustand oder Timeout warten.

| Keyword                                  | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox | Table |
|------------------------------------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|:-----:|
| VerifyValue                              |        |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyValueWCM                           |        |     ✓     |       ✓        |   ✓   |          |          |           |         |       |
| VerifyValueREGX                          |        |     ✓     |       ✓        |   ✓   |          |          |           |         |       |
| VerifyPlaceholder                        |        |     ✓     |       ✓        |       |          |    ✓     |           |         |       |
| VerifyPlaceholderWCM                     |        |     ✓     |       ✓        |       |          |    ✓     |           |         |       |
| VerifyPlaceholderREGX                    |        |     ✓     |       ✓        |       |          |    ✓     |           |         |       |
| VerifyTooltip                            |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyTooltipWCM                         |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyTooltipREGX                        |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyLabel                              |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyLabelWCM                           |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyLabelREGX                          |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyCaption                            |   ✓    |           |                |   ✓   |          |          |           |         |       |
| VerifyCaptionWCM                         |   ✓    |           |                |   ✓   |          |          |           |         |       |
| VerifyCaptionREGX                        |   ✓    |           |                |   ✓   |          |          |           |         |       |
| VerifyAttribute                          |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyAttributeWCM                       |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyAttributeREGX                      |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyExist (generisch)                  |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyHasFocus                           |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |       |
| VerifyListCount                          |        |           |                |       |          |    ✓     |     ✓     |    ✓    |       |
| VerifySelectedCount                      |        |           |                |       |          |    ✓     |     ✓     |    ✓    |       |
| VerifyTableCellValue                     |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableRowContent                    |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableColumnContent                 |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableRowCount                      |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableColumnCount                   |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableHasRow                        |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableContent                       |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableCellValueByHeaders            |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableRowContentByHeader            |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableColumnContentByHeader         |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableCellValueByHeadersREGX        |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableRowContentByHeaderREGX        |        |           |                |       |          |          |           |         |   ✓   |
| VerifyTableColumnContentByHeaderREGX     |        |           |                |       |          |          |           |         |   ✓   |

## 4. Memorize
Kurzbeschreibung: Liest Werte/Attribute und speichert sie in Robot‑Variablen.

| Keyword           | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|-------------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| MemorizeValue     |        |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |           |    ✓    |
| MemorizeTooltip   |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |
| MemorizeLabel     |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |
| MemorizeCaption   |   ✓    |           |                |   ✓   |          |          |           |         |
| MemorizeAttribute |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |

## 5. Log
Kurzbeschreibung: Loggt die aktuellen Werte/Attribute für Diagnosezwecke.

| Keyword      | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|--------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| LogValue     |        |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |           |    ✓    |
| LogTooltip   |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |
| LogLabel     |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |
| LogCaption   |   ✓    |           |                |   ✓   |          |          |           |         |
| LogAttribute |   ✓    |     ✓     |       ✓        |   ✓   |    ✓     |    ✓     |     ✓     |    ✓    |

Hinweise
- VerifyExist: generisch für alle Widgets über `BaseWidget.okw_verify_exist()` (Adapter: `element_exists`).
- TypeKey: Auf Widget‑Ebene nicht implementiert. Das Keyword unterstützt jedoch das Literal `$DELETE` und löscht Inhalte bei textbasierten Widgets (über den Keyword‑Handler), ohne `okw_type_key` zu benötigen.
- Placeholder: Sinnvoll für TextField, MultilineField und input‑basierte ComboBoxen; bei nativen `<select>` ist der Placeholder in der Regel leer.
- Tooltip: Technisch für alle Widgets möglich (liest `title`/`aria-label`), Sinn je nach Element.
- Label: Ermittelt Beschriftung über `aria-labelledby` / `<label for="...">` / `aria-label` / Fallback Text.
- Caption: Sichtbarer Text des Elements selbst (nicht die Feldbeschriftung und nicht der Value‑Inhalt).

Verweise
- Adapter: `src/okw4robot/adapters/selenium_web.py`
- Widgets: `src/okw4robot/widgets/common/*`
- Keywords (Allgemein): `src/okw4robot/keywords/widget_keywords.py`
- Placeholder‑Keywords: `src/okw4robot/keywords/placeholder_keywords.py`
- Tooltip‑Keywords: `src/okw4robot/keywords/tooltip_keywords.py`
- Label‑Keywords: `src/okw4robot/keywords/label_keywords.py`
- Caption‑Keywords: `src/okw4robot/keywords/caption_keywords.py`
- Attribute‑Keywords: `src/okw4robot/keywords/attribute_keywords.py`
- Tabellen‑Keywords: `src/okw4robot/keywords/table_keywords.py`
- Listen‑Keywords: `src/okw4robot/keywords/list_keywords.py`

## 6. Tabellen (Web)
Kurzbeschreibung: Verifikationen für tabellarische Inhalte (nur Web). Tokens und Syntax siehe `docs/table_tokens.md`.

- Basis (Index‑basiert; 1‑basiert, Header ist Zeile 0):
  - `VerifyTableCellValue    <Name>    <Row>    <Col>    <ExpectedWCM>`
  - `VerifyTableRowContent   <Name>    <Row>    <RowPatternWCM>`
  - `VerifyTableColumnContent   <Name>    <Col>    <ColumnPatternWCM>`
  - `VerifyTableRowCount     <Name>    <ExpectedCount>`
  - `VerifyTableColumnCount  <Name>    <ExpectedCount>`
  - `VerifyTableHasRow       <Name>    <RowPatternWCM>`
  - `VerifyTableContent      <Name>    <TablePatternWCM>`

- Header‑basiert (Zeile via WCM‑Key, Spalte via exaktem Header):
  - `VerifyTableCellValueByHeaders         <Name>  <RowKeyWCM>        <ColHeaderExact>  <ExpectedWCM>`
  - `VerifyTableRowContentByHeader         <Name>  <RowHeaderExact>   <RowKeyWCM>       <RowPatternWCM>`
  - `VerifyTableColumnContentByHeader      <Name>  <ColHeaderExact>   <ColumnPatternWCM>`

- Regex‑Varianten (per Zelle via Regex; `$EMPTY` = leere Zelle):
  - `VerifyTableCellValueByHeadersREGX     <Name>  <RowKeyWCM>        <ColHeaderExact>  <ExpectedRegex>`
  - `VerifyTableRowContentByHeaderREGX     <Name>  <RowHeaderExact>   <RowKeyWCM>       <RowRegexes>`
  - `VerifyTableColumnContentByHeaderREGX  <Name>  <ColHeaderExact>   <ColumnRegexes>`

Hinweise
- Wildcards (WCM): `*` = beliebige Sequenz, `?` = ein Zeichen.
- Tokens (Defaults, überschreibbar): `$TAB` (Zellen), `$LF` (Zeilen), `$EMPTY`, `$EMPTYCOL`, `$EMPTYTABLE`.
- Timeouts/Polling: `${OKW_TIMEOUT_VERIFY_TABLE}` (Default z. B. 2s), `${OKW_POLL_VERIFY}` (Default 0.1s).
- Regex in Robot: Backslashes werden in Tabellen oft als Escape interpretiert. Bevorzuge z. B. `[0-9]` statt `\d`, oder escapen doppelt (z. B. `^A3\\d$`).

## 7. Listen (Web)
Kurzbeschreibung: Zählen von Einträgen und Auswahl in listenartigen Widgets.

- `VerifyListCount       <Name>  <ExpectedCount>` → zählt Einträge (ListBox, RadioList, native `<select>`)
- `VerifySelectedCount   <Name>  <ExpectedCount>` → zählt ausgewählte Einträge (Radio meist 0/1)

Hinweise
- Timeouts/Polling: `${OKW_TIMEOUT_VERIFY_LIST}` (Default 2s), `${OKW_POLL_VERIFY}` (Default 0.1s)
- Für Custom‑Combos empfiehlt sich ein eigenes Listen‑Widget im Modell.
