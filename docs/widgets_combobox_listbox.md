# ComboBox & ListBox (Web)

Diese Seite dokumentiert das Verhalten und die Robot-Keywords fÃ¼r ComboBox und ListBox Widgets in OKW4Robot.

---

Hinweis: Die allgemeine Ignore-Regel fÃ¼r leere Werte bzw. `$IGNORE`/`${IGNORE}` (No-Op) gilt auch hier. Details: `docs/keywords_ignore_rule.md`.

## ComboBox
Pfad: `src/okw4robot/widgets/common/combobox.py`

- Konzept: Eingabefeld mit optionaler Dropdown-Auswahl. Unterstützt sowohl native `<select>`-Elemente (nicht editierbar) als auch „type‑ahead“-Combos (editierbar).
- Implementiert:
  - `okw_set_value(value)`: versucht zuerst `select_by_label` (fÃ¼r native `<select>`). Falls das fehlschlÃ¤gt: Feld leeren (`clear_text`), Text tippen (`input_text`) und (wo sinnvoll) mit ENTER bestÃ¤tigen (`press_keys("ENTER")`).
  - `okw_select(value)`: Alias zu `okw_set_value(value)`.
  - `okw_verify_value(expected)`: liest zunÃ¤chst den Eingabewert (`get_value`). Falls leer/nicht verfÃ¼gbar, fÃ¤llt auf das aktuell gewÃ¤hlte Label eines nativen `<select>` zurÃ¼ck (`get_selected_list_labels`, erste Position). Exakter Vergleich, sonst `AssertionError`.
  - `okw_log_value()`: loggt den aktuellen Feldwert (`get_value`).
  - `okw_memorize_value()`: liefert bevorzugt den Feldwert, sonst das ausgewÃ¤hlte Label zurÃ¼ck.
- Typische Adapter-Methoden: `select_by_label`, `clear_text`, `input_text`, `press_keys`, `get_value`, `get_selected_list_labels`.

Robot-Beispiele:
```robotframework
SetValue     myCombobox    Wert
Select       myCombobox    Wert
VerifyValue  myCombobox    Wert
```

Hinweis: Damit sowohl native Selects als auch freie Eingaben funktionieren, ist `SetValue`/`Select` bewusst robust implementiert (Select-by-Label ODER Tippen+ENTER).

---

## ListBox (Mehrfachauswahl)
Pfad: `src/okw4robot/widgets/common/listbox.py`

- Konzept: Mehrfachauswahl basierend auf HTML `<select multiple>`; Auswahl per sichtbarem Label.
- Implementiert:
  - `okw_select(value)`: akzeptiert Einzelwert, Liste oder Komma-separierte Liste. Leere Auswahl fÃ¼hrt zu â€žUnselect Allâ€œ. FÃ¼r Mehrfachauswahl wird `select_by_label(locator, labels[])` verwendet.
  - `okw_verify_value(expected)`: vergleicht die ausgewÃ¤hlten Labels mengenbasiert (reihenfolge-unabhÃ¤ngig) mit der Erwartung; bei Abweichung `AssertionError`.
  - `okw_log_value()`: loggt die aktuell ausgewÃ¤hlten Labels (`get_selected_list_labels`).
  - `okw_memorize_value()`: gibt die Liste der ausgewÃ¤hlten Labels zurÃ¼ck.
- Typische Adapter-Methoden: `select_by_label`, `get_selected_list_labels`, `unselect_all_from_list`.

Robot-Beispiele:
```robotframework
Select       myListBox     Eintrag1, Eintrag2
VerifyValue  myListBox     Eintrag1, Eintrag2
```

Hinweise:
- Kommagetrennte Eingaben werden intern in eine Liste von Labels umgewandelt und getrimmt.
- Eine leere Auswahl (â€žkeine Labelsâ€œ) hebt die gesamte Auswahl auf.

---

Verwandt: Allgemeine Beschreibung der Common-Widgets siehe `docs/widgets_common.md`.


