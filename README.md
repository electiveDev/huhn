# Chicken Tracker (Hühner Tracker)

Chicken Tracker is a simple, functional web application for tracking chicken egg production and food costs. This application helps you calculate average egg production (per day, month, year) and food costs, saving everything in a simple CSV file.
The application interface is fully bilingual (German/English) and can be toggled via the navigation bar.

Eine einfache, funktionale Webanwendung zur Erfassung der Hühnereierproduktion und der Futterkosten. Diese Anwendung hilft Ihnen bei der Berechnung der durchschnittlichen Eierproduktion (pro Tag, Monat, Jahr) und der Futterkosten und speichert alles in einer einfachen CSV-Datei.
Die Anwendungsoberfläche ist vollständig zweisprachig (Deutsch/Englisch) und kann über die Navigationsleiste umgeschaltet werden.

## Features (Funktionen)

- **Dashboard**: See key statistics at a glance / Sehen Sie die wichtigsten Statistiken auf einen Blick:
  - Average eggs per day / Durchschnittliche Eier pro Tag
  - Average eggs per month / Durchschnittliche Eier pro Monat
  - Average eggs per year / Durchschnittliche Eier pro Jahr
  - Average food costs per month / Durchschnittliche Futterkosten pro Monat
  - Total eggs and total costs / Gesamteier und Gesamtkosten
- **Data Entry / Datenerfassung**: Simple form to add daily entries (date, eggs laid, food costs) / Einfaches Formular zum Hinzufügen täglicher Einträge.
- **Entry Management / Verwaltung von Einträgen**: View, edit, and delete existing entries / Anzeigen, Bearbeiten und Löschen vorhandener Einträge.
- **Multilingual / Mehrsprachigkeit**: Switch between German and English at any time / Wechseln Sie jederzeit zwischen Deutsch und Englisch.
- **Simple Storage / Einfache Speicherung**: Data is stored in a local CSV file (`data/data.csv`), making backup or external editing easy / Die Daten werden in einer lokalen CSV-Datei gespeichert.
- **Responsive UI**: Built with Bootstrap 5 for mobile and desktop compatibility / Erstellt mit Bootstrap 5 für Mobil- und Desktop-Kompatibilität.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chicken-tracker
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and navigate to:
   [http://localhost:5000](http://localhost:5000)

## Running Tests

The project includes unit tests to verify data handling logic and application routes.

To run the tests:
```bash
python -m unittest discover tests
```

## Project Structure

- `app.py`: Main Flask application file defining routes.
- `data_handler.py`: Logic for reading/writing CSV and calculating statistics.
- `templates/`: HTML templates (Jinja2) for the frontend.
- `static/`: Static files (CSS).
- `data/`: Directory where `data.csv` is stored.
- `tests/`: Unit tests.
- `translations.py`: Contains translations for German and English.

## Data Storage

All data is stored in `data/data.csv`. The file is automatically created when you add your first entry.
Format: `id,date,type,amount,cost,note`
