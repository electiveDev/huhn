# Chicken Tracker (Hühner Tracker)

Eine einfache, funktionale Webanwendung zur Erfassung der Hühnereierproduktion und der Futterkosten. Diese Anwendung hilft Ihnen bei der Berechnung der durchschnittlichen Eierproduktion (pro Tag, Monat, Jahr) und der Futterkosten und speichert alles in einer einfachen CSV-Datei.

Die Anwendungsoberfläche ist vollständig zweisprachig (Deutsch/Englisch) und kann über die Navigationsleiste umgeschaltet werden.

## Funktionen

- **Dashboard**: Sehen Sie die wichtigsten Statistiken auf einen Blick:
  - Durchschnittliche Eier pro Tag
  - Durchschnittliche Eier pro Monat
  - Durchschnittliche Eier pro Jahr
  - Durchschnittliche Futterkosten pro Monat
  - Gesamteier und Gesamtkosten
- **Datenerfassung**: Einfaches Formular zum Hinzufügen täglicher Einträge (Datum, gelegte Eier, Futterkosten).
- **Verwaltung von Einträgen**: Anzeigen, Bearbeiten und Löschen vorhandener Einträge.
- **Mehrsprachigkeit**: Wechseln Sie jederzeit zwischen Deutsch und Englisch.
- **Einfache Speicherung**: Die Daten werden in einer lokalen CSV-Datei (`data/data.csv`) gespeichert, was die Sicherung oder externe Bearbeitung erleichtert.
- **Responsive UI**: Erstellt mit Bootstrap 5 für Mobil- und Desktop-Kompatibilität.

## Voraussetzungen

- **Python 3.8+**
- **pip** (Python-Paketinstallationsprogramm)

## Installation

1. **Repository klonen:**
   ```bash
   git clone <repository-url>
   cd chicken-tracker
   ```

2. **Virtuelle Umgebung erstellen (optional, aber empfohlen):**
   ```bash
   python -m venv venv
   # Unter Windows
   venv\Scripts\activate
   # Unter macOS/Linux
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

## Anwendung starten

1. **Starten Sie den Flask-Server:**
   ```bash
   python app.py
   ```

2. **Zugriff auf die Anwendung:**
   Öffnen Sie Ihren Webbrowser und navigieren Sie zu:
   [http://localhost:5000](http://localhost:5000)

## Tests ausführen

Das Projekt enthält Unit-Tests, um die Datenverarbeitungslogik und die Anwendungsrouten zu überprüfen.

So führen Sie die Tests aus:
```bash
python -m unittest discover tests
```

## Projektstruktur

- `app.py`: Hauptdatei der Flask-Anwendung, die Routen definiert.
- `data_handler.py`: Logik zum Lesen/Schreiben von CSV und Berechnen von Statistiken.
- `templates/`: HTML-Vorlagen (Jinja2) für das Frontend.
- `static/`: Statische Dateien (CSS).
- `data/`: Verzeichnis, in dem `data.csv` gespeichert wird.
- `tests/`: Unit-Tests.
- `translations.py`: Enthält die Übersetzungen für Deutsch und Englisch.

## Datenspeicherung

Alle Daten werden in `data/data.csv` gespeichert. Die Datei wird automatisch erstellt, wenn Sie Ihren ersten Eintrag hinzufügen.
Format: `id,date,type,amount,cost,note`
