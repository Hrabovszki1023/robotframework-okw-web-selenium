# Dokumentation – okw-web-selenium

Selenium-spezifische Dokumentation fuer `robotframework-okw-web-selenium`.

> Generische Keyword-Vertraege, Contract und Spezifikation: siehe
> [robotframework-okw4robot/docs/](http://192.168.1.130:3000/Hrabovszki1023/robotframework-okw4robot/src/branch/main/docs)

---

## Widget-Implementierung

- [Web_Widget_Matrix.md](Web_Widget_Matrix.md) – Welche HTML-Elemente von welchem WebSe_*-Widget abgedeckt werden
- [widgets_combobox_listbox.md](widgets_combobox_listbox.md) – WebSe_ComboBox und WebSe_ListBox im Detail
- [radiolist.md](radiolist.md) – WebSe_RadioList: Radio-Button-Gruppen, Locator-Strategien
- [implementation/selenium/README.md](implementation/selenium/README.md) – Selenium-Implementierungshinweise

## Host / App / Konfiguration

- [docs_host_app_config.md](docs_host_app_config.md) – YAML-Konfiguration fuer Host und App (Chrome, Firefox)
- [docs_host_app_trennung.md](docs_host_app_trennung.md) – Architektur: Trennung Host vs. App

## ExecuteJS

- [executejs-snippets.md](executejs-snippets.md) – JavaScript-Snippets fuer das ExecuteJS-Keyword

## Diagramme (PlantUML)

- [diagramms/adapters_overview.puml](diagramms/adapters_overview.puml) – Adapter-Uebersicht
- [diagramms/adapters_sequence.puml](diagramms/adapters_sequence.puml) – Keyword → Widget → Adapter Sequenz
- [diagramms/widgets_inheritance.puml](diagramms/widgets_inheritance.puml) – WebSe_*-Klassenhierarchie
- [diagramms/sync_read.puml](diagramms/sync_read.puml) – Synchronisation bei Lese-Operationen
- [diagramms/sync_write.puml](diagramms/sync_write.puml) – Synchronisation bei Schreib-Operationen

## Beispiele (HTML)

- [examples/widgets_demo.html](examples/widgets_demo.html) – Demo-Seite fuer WidgetsDemo-Tests
- [examples/table_demo.html](examples/table_demo.html) – Demo-Seite fuer Table-Tests

## Entwicklung

- [dev/TESTING.md](dev/TESTING.md) – Testverfahren
- [dev/RELEASING.md](dev/RELEASING.md) – Release-Checkliste

## Sonstiges

- [presentations/OKW4Robot_Benefits.md](presentations/OKW4Robot_Benefits.md) – Vorteile des OKW-Ansatzes
