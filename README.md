# Chicken Tracker (Hühner Tracker)

A simple, functional web application to track chicken egg production and food costs. This application helps you calculate average egg production (per day, month, year) and food costs, storing everything in a simple CSV file.

The application interface is fully localized in German.

## Features

- **Dashboard**: View key statistics at a glance:
  - Average Eggs per Day
  - Average Eggs per Month
  - Average Eggs per Year
  - Average Food Cost per Month
  - Total Eggs and Total Cost
- **Data Entry**: Easy form to add daily records (Date, Eggs Laid, Food Cost).
- **Record Management**: View, Edit, and Delete existing records.
- **Simple Storage**: Data is persisted in a local CSV file (`data/data.csv`), making it easy to backup or manipulate externally.
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

The project includes unit tests to verify the data handling logic and application routes.

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

## Data Storage

All data is stored in `data/data.csv`. The file is automatically created when you add your first record.
Format: `id,date,eggs,food_cost`
