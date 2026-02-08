# Objektzustände (GUI/Web)

Diese Seite strukturiert zentrale Zustände von GUI-/Web‑Widgets in OKW4Robot, zeigt ihre Beziehungen und liefert eine kompakte Matrix, wie zusammengesetzte Fähigkeiten (z. B. „klickbar“) aus Basis‑Eigenschaften entstehen.

---

## Ziele

- Gemeinsames Vokabular für Zustände („enabled“, „editable“, „focusable“, …).
- Klarer Unterschied zwischen „hat Fokus“ und „ist aktiv (enabled)“.
- Ableitung zusammengesetzter Fähigkeiten (z. B. „klickbar“, „typbar“).
- Bezug zu vorhandenen/fehlenden Robot‑Keywords in OKW4Robot.

---

## Basis‑Eigenschaften (Definitionen)

- Existiert: Element ist im DOM auffindbar.
  - OKW: `VerifyExist    <Name>    YES|NO` (siehe `src/okw4robot/keywords/widget_keywords.py:159`).
- Sichtbar: Element ist sichtbar (nicht `display:none`/`visibility:hidden`) und erscheint im Viewport.
  - OKW: implizite Prüfung vor Aktionen (Sync), vgl. `docs/synchronization_strategy.md: exists → visible`.
- Aktiv/Enabled: Nicht deaktiviert; Interaktion grundsätzlich möglich (z. B. kein `disabled`).
  - OKW: Adapter‐Hook `is_enabled(...)` vorhanden (`src/okw4robot/adapters/selenium_web.py:111`).
- Editierbar: Wert kann geändert werden (nicht `readonly`; `contenteditable` gilt als editierbar).
  - OKW: Adapter‐Hook `is_editable(...)` vorhanden (`src/okw4robot/adapters/selenium_web.py:118`).
- Fokusierbar: Kann Fokus erhalten (theoretisch), unabhängig davon, ob es ihn aktuell hat.
  - OKW: nicht explizit geprüft; meist implizit über Widget‑/Browserlogik.
- Fokussiert: Hat aktuell den Tastaturfokus (aktives Element).
  - OKW: `VerifyHasFocus    <Name>    YES|NO` (siehe `src/okw4robot/keywords/widget_keywords.py:193`).

Hinweis: Vor schreibenden Aktionen prüft OKW4Robot standardmäßig „existiert → sichtbar → enabled → (optional) editierbar“; Details: `src/okw4robot/widgets/base/base_widget.py:71` ff. und `docs/synchronization_strategy.md`.

---

## Zusammengesetzte Fähigkeiten (abgeleitet)

Die folgenden Fähigkeiten lassen sich aus Basis‑Eigenschaften ableiten. „Erforderlich“ bedeutet: muss typischerweise erfüllt sein, damit die Fähigkeit verlässlich nutzbar ist.

```
Fähigkeit        | Existiert | Sichtbar | Enabled | Editierbar | Fokusierbar | Fokussiert
-----------------|----------:|---------:|--------:|-----------:|------------:|----------:
Klickbar         |     Ja    |    Ja    |   Ja    |     –      |      –      |     –
Typbar           |     Ja    |    Ja    |   Ja    |     Ja     |     Ja      |     –
SelektierbarText |     Ja    |    Ja    |   Ja    |     Nein   |     Ja      |     –
Fokusierbar      |     Ja    |    –     |   –     |     –      |     Ja      |     –
Fokussiert       |     Ja    |    –     |   –     |     –      |     Ja      |     Ja
LesbarWert       |     Ja    |  (oft)   |   –     |     –      |      –      |     –
```

Erläuterungen:
- Klickbar: Praktisch auch „nicht verdeckt“ (Overlays) – dies wird projektseitig via Busy‑Selektoren in der Sync adressiert (`until_not_visible`).
- Typbar: Trifft typischerweise auf Textfelder zu; bei `contenteditable` ebenfalls erfüllt.
- SelektierbarText: Read‑only Eingabefelder – markieren/kopieren möglich, aber nicht änderbar.
- LesbarWert: Sichtbarkeit ist für viele DOM‑Reads nicht zwingend, aber in UI‑Tests häufig erwünscht; OKW‑Sync konfiguriert dies je nach Intent.

---

## Zustands‑Beziehungen (Heuristik)

- Fokussiert ⇒ fokusierbar.
- Editierbar ⇒ enabled.
- Enabled ⇏ editierbar (z. B. `readonly`).
- Klickbar ≈ sichtbar ∧ enabled ∧ nicht verdeckt.
- Typbar ≈ sichtbar ∧ enabled ∧ editierbar ∧ fokusierbar.
- SelektierbarText ≈ sichtbar ∧ enabled ∧ ¬editierbar ∧ fokusierbar.

---

## Beispiele (typische Kombinationen)

```
Szenario                         | Existiert | Sichtbar | Enabled | Editierbar | Fokusierbar | Fokussiert
---------------------------------|----------:|---------:|--------:|-----------:|------------:|----------:
Readonly‑Textfeld                |    Ja     |   Ja     |   Ja    |    Nein    |     Ja      |   (var.)
Aktives editierbares Textfeld    |    Ja     |   Ja     |   Ja    |    Ja      |     Ja      |   (var.)
Deaktivierter Button             |    Ja     |   Ja     |   Nein  |     –      |     (nein)  |    –
Verdecktes Element (Overlay)     |    Ja     |   Nein   |   –     |     –      |      –      |    –
Element mit Fokus (Cursor)       |    Ja     |  (Ja)    |  (Ja)   |   (var.)   |     Ja      |    Ja
```

„(var.)“: kann je nach Widget/DOM abweichen; Klammern kennzeichnen keine harte Voraussetzung.

---

## OKW4Robot: Verify‑Keywords (mit Timeout)

Vorhanden (alle mit Timeout‑Semantik via Polling)
- `VerifyExist       <Name>    YES|NO` → Existenz prüfen.
- `VerifyVisible     <Name>    YES|NO` → Sichtbarkeit prüfen (Adapter `is_visible`).
- `VerifyEnabled     <Name>    YES|NO` → Aktiv/Enabled prüfen (Adapter `is_enabled`).
- `VerifyEditable    <Name>    YES|NO` → Editierbar/Readonly prüfen (Adapter `is_editable`).
- `VerifyFocusable   <Name>    YES|NO` → Fokusierbarkeit prüfen (Adapter `is_focusable`).
- `VerifyClickable   <Name>    YES|NO` → Klickbarkeit prüfen (Adapter `is_clickable`).
- `VerifyHasFocus    <Name>    YES|NO` → aktuellen Fokuszustand prüfen (Adapter `has_focus`).
- `VerifyValue*      <Name>    …` → Werte‑Prüfungen inkl. WCM/REGX (bereits mit Timeout).

Adapter‑Anforderung und Fehlerbild
- Fehlt eine benötigte Adapter‑Methode, brechen die Keywords mit RuntimeError ab und nennen Keyword‑Name, Widget‑Name/‑Klasse, Adapter‑Klasse, Methode und den Locator.

Konfiguration (Defaults in Klammern)
- `${OKW_TIMEOUT_VERIFY_EXIST}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_VISIBLE}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_ENABLED}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_EDITABLE}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_FOCUSABLE}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_CLICKABLE}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_FOCUS}` (2.0 s)
- `${OKW_TIMEOUT_VERIFY_VALUE}` (10 s; bestehend)
- `${OKW_POLL_VERIFY}` (0.1 s)

Hinweis: Unabhängig davon bleibt die implizite Sync vor schreibenden Aktionen aktiv (`exists → visible → enabled → editable`), konfigurierbar über `docs/synchronization_strategy.md`.

---

## Konfiguration und weitere Hinweise

- Synchronisationsstrategie und globale Variablen: `docs/synchronization_strategy.md`.
- Zuordnung der Widget‑Keywords: `docs/widgets_common.md`.
- Host/App‑Kontexte: `docs/keywords_host_app.md`.

---

## Glossar (kurz)

- Enabled/Aktiv: Interaktion erlaubt (kein `disabled`).
- Editierbar: Wert veränderbar (nicht `readonly`, ggf. `contenteditable`).
- Fokusierbar: Kann Fokus erhalten (theoretisch).
- Fokussiert: Hat aktuell den Fokus.
- Klickbar: Praktikabel klickbar (sichtbar, enabled, nicht verdeckt).
- Selektierbar (Text): Inhalt kann markiert/kopiert werden, aber nicht geändert.
