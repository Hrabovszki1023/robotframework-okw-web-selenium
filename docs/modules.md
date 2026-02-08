# 🧭 Modulübersicht für OKW4Robot

## `okw4robot/__init__.py`
Initialisiert das OKW4Robot-Paket.

## `okw4robot/adapters/__init__.py`
Initialisierung des Adapter-Moduls.

## `okw4robot/adapters/base.py`
Definiert die UiAdapter-Basisklasse für generische Adapterfunktionen.

## `okw4robot/adapters/selenium_web.py`
Implementiert den Selenium-Webadapter für Browserinteraktion.

## `okw4robot/keywords/__init__.py`
Initialisiert die Robot Framework Schlüsselwortmodule.

## `okw4robot/keywords/app.py`
Stellt App-bezogene Keywords bereit (Start App, Select Window etc.).

## `okw4robot/keywords/host.py`
Stellt Host-bezogene Keywords bereit (Start Host, Stop Host etc.).

## `okw4robot/keywords/widget_keywords.py`
Stellt Widget-bezogene Keywords bereit (ClickOn, SetValue etc.).

## `okw4robot/locators/__init__.py`
Initialisiert das Lokatoren-Untermodul.

## `okw4robot/runtime/context.py`
Verwaltet den aktuellen Testkontext (Adapter, App, Window).

## `okw4robot/utils/loader.py`
Lädt Python-Klassen aus Strings (z. B. aus YAML).

## `okw4robot/utils/logging_mixin.py`
Stellt ein LoggingMixin zur Verfügung, um Klassennamen + Methoden strukturiert zu loggen.

## `okw4robot/utils/yaml_loader.py`
Lädt YAML-Dateien mit Fallback-Strategie: Projektverzeichnis → Framework-Paket.

## `okw4robot/widgets/base/BaseWidget.py`
Basisklasse für alle GUI-Widgets mit OKW-Methodenschnittstelle.

## `okw4robot/widgets/host/browsercontrol/BrowserControl.py`
Widget für browserbezogene Aktionen wie Maximieren.

## `okw4robot/widgets/host/browsercontrol/UrlBar.py`
Widget für URL-Eingabe (z. B. für go_to-Logik).
