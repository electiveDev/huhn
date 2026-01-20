# Chicken Tracker (Hühner-Tracker)

Eine einfache, funktionale Webanwendung zur Erfassung der Hühnereierproduktion und der Futterkosten. Diese Anwendung hilft Ihnen bei der Berechnung der durchschnittlichen Eierproduktion (pro Tag, Monat, Jahr) und der Futterkosten, wobei alles in einer einfachen CSV-Datei gespeichert wird.

Die Benutzeroberfläche der Anwendung ist vollständig auf Deutsch lokalisiert.

## Funktionen

- **Dashboard**: Sehen Sie wichtige Statistiken auf einen Blick:
  - Durchschnittliche Eier pro Tag
  - Durchschnittliche Eier pro Monat
  - Durchschnittliche Eier pro Jahr
  - Durchschnittliche Futterkosten pro Monat
  - Gesamtzahl Eier und Gesamtkosten
- **Dateneingabe**: Einfaches Formular zum Hinzufügen von Einträgen (Eier, Futter, Hühner).
- **Verwaltung der Einträge**: Ansehen, Bearbeiten und Löschen vorhandener Einträge.
- **Einfache Speicherung**: Daten werden in einer lokalen CSV-Datei (`data/data.csv`) gespeichert, was die Sicherung oder externe Bearbeitung erleichtert.
- **Responsive Benutzeroberfläche**: Erstellt mit Bootstrap 5 für Kompatibilität auf Mobilgeräten und Desktops.

## Voraussetzungen

- **Python 3.8+**
- **pip** (Python-Paketmanager)

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

## Starten der Anwendung

1. **Starten des Flask-Servers:**
   ```bash
   python app.py
   ```

2. **Zugriff auf die Anwendung:**
   Öffnen Sie Ihren Webbrowser und navigieren Sie zu:
   [http://localhost:5000](http://localhost:5000)

## Tests ausführen

Das Projekt enthält Unit-Tests, um die Datenverarbeitungslogik und die Anwendungsrouten zu überprüfen.

Um die Tests auszuführen:
```bash
python -m unittest discover tests
```

## Projektstruktur

- `app.py`: Haupt-Flask-Anwendungsdatei, die die Routen definiert.
- `data_handler.py`: Logik zum Lesen/Schreiben von CSV und zur Berechnung von Statistiken.
- `templates/`: HTML-Vorlagen (Jinja2) für das Frontend.
- `static/`: Statische Dateien (CSS).
- `data/`: Verzeichnis, in dem `data.csv` gespeichert wird.
- `tests/`: Unit-Tests.

## Datenspeicherung

Alle Daten werden in `data/data.csv` gespeichert. Die Datei wird automatisch erstellt, wenn Sie Ihren ersten Eintrag hinzufügen.
Format: `id,date,type,amount,cost,note`
