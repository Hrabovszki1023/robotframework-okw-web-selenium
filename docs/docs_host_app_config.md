# 🧩 YAML-Konfiguration: Hosts und Anwendungen

Diese Datei beschreibt die Struktur und Bedeutung der Parameter im YAML-Konfigurationsabschnitt für JavaRPC-Hosts und eingebettete Java-Anwendungen.

## 📁 Beispielstruktur

```yaml
hosts:
  JavaRPC:
    type: JavaRPC
    host: localhost
    port: 5678
    jar: ../JavaRPCServer/target/java-rpc-server-1.0-SNAPSHOT-jar-with-dependencies.jar
    app:
      SwingSet3:
        jar: C:/tools/SwingSet3.jar
        args: []  # Optional: zusätzliche Startargumente
```

## 🧾 Parameterbeschreibung

### 🔹 `hosts`
Hauptabschnitt für alle konfigurierten Hosts.

### 🔹 `JavaRPC`
Der Name des Hosts (frei wählbar, eindeutiger Bezeichner).

| Schlüssel     | Beschreibung                                                                 |
|---------------|------------------------------------------------------------------------------|
| `type`        | Adaptertyp, aktuell `JavaRPC`.                                               |
| `host`        | Adresse des Servers, z. B. `localhost` oder eine IP-Adresse.                 |
| `port`        | Portnummer, auf dem der Java-RPC-Server erreichbar ist.                      |
| `jar`         | Pfad zur JavaRPC-Server-JAR (wird bei `localhost` automatisch gestartet).    |
| `app`         | Abschnitt für eingebettete Java-Apps, z. B. `SwingSet3`.                     |

### 🔹 `app`
Untergeordnete Anwendungen, die im Kontext des Hosts gestartet werden.

| Schlüssel     | Beschreibung                                                                |
|---------------|-----------------------------------------------------------------------------|
| `jar`         | Pfad zur ausführbaren Anwendungs-JAR.                                       |
| `args`        | Liste zusätzlicher Argumente beim Start der Anwendung. Optional.           |

## ✅ Hinweise

- Mehrere Hosts können parallel definiert werden.
- Der Eintrag `jar` beim Host ist **nur bei lokalen Servern erforderlich**.
- Die App-JARs werden über das JavaRPC-Protokoll gestartet.

---

© 2025 – OpenKeyWord / OKW4Robot
