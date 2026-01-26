# Chicken Tracker

A simple, functional web application for tracking chicken egg production and food costs. This application helps you calculate average egg production (per day, month, year) and food costs, saving everything in a simple CSV file.

The user interface is fully bilingual (German/English) and can be toggled via the navigation bar.

## Features

- **Dashboard**: See key statistics at a glance:
  - **Stock**: Current number of chickens.
  - **Production**: Average eggs per day.
  - **Efficiency**: Cost per egg (calculated from total food and chicken costs).
  - **Costs**:
    - Average food costs per month and year.
    - Current year's food cost.
    - Total costs (food + chicken purchases).
- **Data Entry**: Simple tabbed forms to add:
  - **Eggs**: Daily egg count.
  - **Food**: Food purchase (weight and cost).
  - **Chickens**: Stock changes (buy/sell/loss) with associated costs.
- **Entry Management**: View, edit, and delete existing entries.
- **Multilingual**: Switch between German and English at any time.
- **Dark Mode**: Designed with a dark theme for comfortable viewing.
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

- `type`: 'egg', 'food', or 'chicken'.
- `amount`: Polymorphic field.
  - For `egg` and `chicken`: Integer (quantity).
  - For `food`: Float (weight in kg).
- `cost`: Monetary value in €.
