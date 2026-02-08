# Trennung von Testlogik und technischen Parametern in OKW4Robot (JavaRPC)

Dieses Dokument beschreibt das Architekturprinzip, wie im OKW4Robot-Projekt die **abstrakte Testlogik** von den **technischen Parametern** (wie Pfade, Ports, Jar-Dateien) getrennt wird.

---

## 1. Technische Parameter: Aus der Objektlisten-YAML

Die technischen Details zum JavaRPC-Host und den eingebetteten Swing-Anwendungen werden zentral in einer YAML-Datei gepflegt. Beispiel:

```yaml
JavaRPC:
  __self__:
    class: okw4robot.adapters.javaRPC.java_rpc_adapter.JavaRpcAdapter

  SwingSet3:
    __self__:
      jar: C:/tools/SwingSet3.jar
      main_class: SwingSet3
      port: 5678
```

Diese Angaben werden beim Start des Hosts verwendet, um z. B. automatisch die Anwendung zu starten und die Verbindung herzustellen.

---

## 2. Abstrakte Testlogik: In den Robot-Testfällen

Die Robot-Testfälle enthalten **nur noch abstrakte Schlüsselwörter und App-/Widget-Namen**, z. B.:

```robot
Start Host    JavaRPC
Select App    SwingSet3
Click         MainWindow.OK
Verify Text   MainWindow.Hilfe    Hilfe
```

Alle konkreten Lokatoren (z. B. `by_name: "helpButton"`) werden automatisch zur Laufzeit über die YAML-Datei aufgelöst.

---

## 3. Vorteile der Trennung

Diese Struktur hat entscheidende Vorteile:

- ✅ **Wiederverwendbarkeit**: Derselbe Test kann für mehrere Java-Swing-Anwendungen verwendet werden – nur durch Austausch der YAML.
- ✅ **Technologie-Kapselung**: Die Testfälle bleiben gleich, auch wenn sich die GUI-Technologie ändert (z. B. von Swing auf JavaFX).
- ✅ **Wartbarkeit**: Änderungen an Ports, Pfaden, jar-Dateien oder Fensterklassen erfolgen ausschließlich in der YAML.
- ✅ **Remote-Tests**: Einfache Umschaltung zwischen lokalem und Remote-RPC-Server durch Änderung der `host`-Angabe in der YAML.

---

## 4. Beispiel-Testfall

```robot
*** Test Cases ***
Login erfolgreich
    Start Host    JavaRPC
    Select App    MeineFirmaFormular
    Click         LoginDialog.Anmelden
    Verify Text   LoginDialog.Status     Willkommen
```

---

## 5. Fazit

Diese Architektur folgt strikt dem Prinzip **„abstrakt im Test, konkret in der YAML“**.  
Damit wird Testautomatisierung robust, wartbar und skalierbar – ohne hartkodierte technische Details in den Testfällen.