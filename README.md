# Chicken Tracker

A simple, functional web application for tracking chicken egg production and food costs. This application helps you calculate average egg production (per day, month, year) and food costs, saving everything in a simple CSV file.

The user interface is fully bilingual (German/English) and can be toggled via the navigation bar.

## Features

- **Dashboard**: Get key statistics at a glance:
  - **Stock**: Current number of chickens.
  - **Production**: Average eggs per day.
  - **Efficiency**: Cost per egg (calculated from total food and chicken costs).
  - **Costs**: Average food costs and total expenses.
- **Data Entry**: Simple tabbed forms to add:
  - **Eggs**: Daily egg count.
  - **Food**: Food purchase (weight and cost).
  - **Chickens**: Stock changes (buy/sell/loss) with associated costs.
- **Entry Management**: View, edit, and delete existing entries.
- **Multilingual**: Switch between German and English at any time.
- **Dark Mode**: Designed with a dark theme for comfortable viewing.
- **Simple Storage**: Data is stored in a local CSV file (`data/data.csv`), making backup or external editing easy.
- **Responsive UI**: Built with Bootstrap 5 for mobile and desktop compatibility.
