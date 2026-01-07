import pandas as pd
import uuid
import os
from datetime import datetime

DATA_FILE = 'data/data.csv'

def _ensure_file_exists():
    directory = os.path.dirname(DATA_FILE)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=['id', 'date', 'type', 'amount', 'cost', 'note'])
        df.to_csv(DATA_FILE, index=False)

def get_all_records():
    _ensure_file_exists()
    try:
        df = pd.read_csv(DATA_FILE)
        if df.empty:
            return []

        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date', ascending=False)

        # Display format
        df['display_date'] = df['date'].dt.strftime('%d/%m/%Y')
        # Keep raw date for editing
        df['raw_date'] = df['date'].dt.strftime('%Y-%m-%d')

        records = df.to_dict('records')
        # Remap type to German for display
        type_map = {'egg': 'Eier', 'food': 'Futter', 'chicken': 'Hühner'}

        # Replace NaN with empty string
        df = df.fillna('')
        records = df.to_dict('records')

        for r in records:
            r['date'] = r['display_date']
            r['type_display'] = type_map.get(r['type'], r['type'])

        return records
    except pd.errors.EmptyDataError:
        return []

def add_record(date, record_type, amount=0, cost=0.0, note=""):
    _ensure_file_exists()

    amount_val = 0
    if record_type == 'food':
        amount_val = float(amount) if amount else 0.0
    else:
        amount_val = int(amount) if amount else 0

    new_record = {
        'id': str(uuid.uuid4()),
        'date': date,
        'type': record_type,
        'amount': amount_val,
        'cost': float(cost) if cost else 0.0,
        'note': str(note) if note else ""
    }
    df = pd.DataFrame([new_record])
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)
    return new_record['id']

def get_record(record_id):
    _ensure_file_exists()
    df = pd.read_csv(DATA_FILE)
    record = df[df['id'] == record_id]
    if not record.empty:
        # Replace NaN with empty string/None for form handling
        record = record.fillna('')
        return record.iloc[0].to_dict()
    return None

def update_record(record_id, date, amount, cost, note, record_type=None):
    _ensure_file_exists()
    df = pd.read_csv(DATA_FILE)
    if record_id in df['id'].values:
        current_type = df.loc[df['id'] == record_id, 'type'].iloc[0]

        # If new type is provided, use it; otherwise keep current
        new_type = record_type if record_type else current_type

        amount_val = 0
        if new_type == 'food':
            amount_val = float(amount) if amount else 0.0
        else:
            # Handle float strings like "10.5" by casting to float first
            amount_val = int(float(amount)) if amount else 0

        # For eggs, cost should be 0.0
        cost_val = 0.0 if new_type == 'egg' else (float(cost) if cost else 0.0)

        df.loc[df['id'] == record_id, ['date', 'type', 'amount', 'cost', 'note']] = [date, new_type, amount_val, cost_val, note]
        df.to_csv(DATA_FILE, index=False)
        return True
    return False

def delete_record(record_id):
    _ensure_file_exists()
    df = pd.read_csv(DATA_FILE)
    if record_id in df['id'].values:
        df = df[df['id'] != record_id]
        df.to_csv(DATA_FILE, index=False)
        return True
    return False

def get_statistics():
    _ensure_file_exists()
    try:
        df = pd.read_csv(DATA_FILE)
        if df.empty:
            return _empty_stats()

        df['date'] = pd.to_datetime(df['date'])

        # --- Filters ---
        # Explicit copy to avoid SettingWithCopyWarning
        eggs_df = df[df['type'] == 'egg'].copy()
        food_df = df[df['type'] == 'food'].copy()
        chicken_df = df[df['type'] == 'chicken'].copy()

        # --- Chicken Stats ---
        current_chickens = chicken_df['amount'].sum()

        # --- Egg Stats ---
        total_eggs = eggs_df['amount'].sum()
        days_recorded = eggs_df['date'].nunique()
        avg_eggs_day = total_eggs / days_recorded if days_recorded > 0 else 0

        if not eggs_df.empty:
            eggs_df['month'] = eggs_df['date'].dt.to_period('M')
            monthly_eggs_stats = eggs_df.groupby('month')['amount'].sum()
            avg_eggs_month = monthly_eggs_stats.mean()

            eggs_df['year'] = eggs_df['date'].dt.to_period('Y')
            yearly_eggs_stats = eggs_df.groupby('year')['amount'].sum()
            avg_eggs_year = yearly_eggs_stats.mean()
        else:
            avg_eggs_month = 0
            avg_eggs_year = 0

        # --- Food Stats ---
        if not food_df.empty:
            food_df['month'] = food_df['date'].dt.to_period('M')
            monthly_food_cost = food_df.groupby('month')['cost'].sum()
            avg_food_cost_month = monthly_food_cost.mean()

            food_df['year'] = food_df['date'].dt.to_period('Y')
            yearly_food_cost_sum = food_df.groupby('year')['cost'].sum()
        else:
            avg_food_cost_month = 0
        # Just getting the sum for the current year would be better, but "Statistik übers ganze Jahr"
        # usually implies total cost per year. Let's provide the average yearly cost or just total?
        # User said: "monatskosten und kosten pro jahr" -> Monthly Costs and Costs per Year.
        # Let's provide Avg Monthly Cost and Total Cost Last Year (or avg yearly).
        # For simplicity in the dashboard, let's show Avg Monthly.

        total_food_cost = food_df['cost'].sum()

        # --- Cost per Egg Logic ---
        # Cost per Egg = (Total Food Cost + Total Chicken Cost) / Total Eggs
        # Note: This is an overall average "production cost".
        total_chicken_cost = chicken_df['cost'].sum() # Cost to buy chickens

        # Net cost? If selling chickens returns money (negative cost?), we sum it.
        # Assuming 'cost' column is positive for expense.

        overall_cost = total_food_cost + total_chicken_cost
        cost_per_egg = overall_cost / total_eggs if total_eggs > 0 else 0

        return {
            'avg_eggs_day': round(avg_eggs_day, 2),
            'avg_eggs_month': round(avg_eggs_month, 2),
            'avg_eggs_year': round(avg_eggs_year, 2),
            'avg_food_cost_month': round(avg_food_cost_month, 2),
            'current_chickens': int(current_chickens),
            'cost_per_egg': round(cost_per_egg, 2),
            'total_eggs': int(total_eggs),
            'total_food_cost': round(total_food_cost, 2),
            'total_chicken_cost': round(total_chicken_cost, 2)
        }
    except Exception as e:
        print(f"Error calculating stats: {e}")
        return _empty_stats()

def _empty_stats():
    return {
        'avg_eggs_day': 0,
        'avg_eggs_month': 0,
        'avg_eggs_year': 0,
        'avg_food_cost_month': 0,
        'current_chickens': 0,
        'cost_per_egg': 0,
        'total_eggs': 0,
        'total_food_cost': 0,
        'total_chicken_cost': 0
    }
