Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2025-10-19

Highlights
- Packaging for PyPI: pyproject.toml configured for src/ layout; URLs set; Python >= 3.10.
- Licensing: Community (non‑commercial) LICENSE with explicit AS‑IS warranty disclaimer and liability limitation; COMMERCIAL_LICENSE.md and docs/license_faq.md added.
- Web widget matrix refreshed and normalized (UTF‑8, ✓ marks). Table + List keywords integrated in overview.

Features
- SetValue: $EMPTY implemented and documented; $IGNORE behavior clarified.
- TypeKey: Documented; supports $DELETE to clear content.
- Select: Documented.
- Verify value family: VerifyValue, VerifyValueWCM, VerifyValueREGX documented.
- Verify exist/log/memorize: VerifyExist, LogValue, MemorizeValue documented; SetFocus + VerifyHasFocus documented.
- Verify “Is*” rename: VerifyVisible/Enabled/Editable/Focusable/Clickable → VerifyIsVisible/IsEnabled/IsEditable/IsFocusable/IsClickable; keyword docs added.
- ExecuteJS: Comprehensive docs, plus docs/executejs-snippets.md with project‑specific one‑liners.
- Tooltip: VerifyTooltip/…WCM/…REGX documented.
- Tables:
  - Documentation for VerifyTable* (row/column/cell/hasRow/counts/content).
  - Header‑based selection keywords: VerifyTableCellValueByHeaders, VerifyTableRowContentByHeader, VerifyTableColumnContentByHeader.
  - Regex variants for header‑based: …ByHeadersREGX/…ByHeaderREGX.
  - Implementation helpers in table keywords: header name resolution and row key matching.
- Lists:
  - New list keywords: VerifyListCount, VerifySelectedCount (library: ListKeywords).
  - Widget methods: BaseWidget stubs, implementations in ListBox, RadioList, ComboBox (native <select> support; input‑based selected count 0/1).

Docs
- Added docs/keywords_table_headers.md (header‑based + REGX table docs).
- Added docs/keywords_list.md (list count/select keywords).
- Added regex best practices: docs/regex_best_practices.md; linked from docs and matrix; REGX docs updated with backslash guidance.
- Web_Widget_Matrix.md rebuilt (UTF‑8, consistent with all keywords).

Tests
- Table tests: Web_Table_VerifyByHeaders.robot and Web_Table_VerifyByHeadersREGX.robot.
- List tests: Web_List_VerifyCounts.robot.
- Fixed run.ps1 line continuation for including all suites; converted WidgetsDemo.robot to UTF‑8.

Breaking changes
- Keyword renames: VerifyVisible/VerifyEnabled/VerifyEditable/VerifyFocusable/VerifyClickable → VerifyIsVisible/IsEnabled/IsEditable/IsFocusable/IsClickable.
  - External suites must update calls to the new names.

Upgrade notes
- Ensure your suites use the new VerifyIs* keywords.
- For regex patterns in Robot tables prefer character classes (e.g., `[0-9]`) or double‑escape backslashes (e.g., `^A3\\d$`).

Compatibility
- Python: >= 3.10

License
- Community (non‑commercial) license with AS‑IS and liability disclaimer; commercial usage requires a separate license.

[0.2.0]: https://github.com/Hrabovszki1023/okw4robot/releases/tag/v0.2.0
