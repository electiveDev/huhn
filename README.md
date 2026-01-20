# Chicken Tracker

A simple, functional web application for tracking chicken egg production and food costs. This application helps you calculate average egg production (per day, month, year) and food costs, saving everything in a simple CSV file.

The user interface is fully bilingual (German/English) and can be toggled via the navigation bar.

## Features

- **Dashboard**: See key statistics at a glance:
  - Average eggs per day
  - Average eggs per month
  - Average eggs per year
  - Average food costs per month
  - Total eggs and total costs
- **Data Entry**: Simple form to add daily entries (date, eggs laid, food costs).
- **Entry Management**: View, edit, and delete existing entries.
- **Multilingual**: Switch between German and English at any time.
- **Simple Storage**: Data is stored in a local CSV file (`data/data.csv`), making backup or external editing easy.
- **Responsive UI**: Built with Bootstrap 5 for mobile and desktop compatibility.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chicken-tracker
   ```

2. **Create a virtual environment (optional, but recommended):**
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

## Start Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and navigate to:
   [http://localhost:5000](http://localhost:5000)

## Run Tests

The project includes unit tests to verify data processing logic and application routes.

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
