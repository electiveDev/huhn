import pandas as pd
import uuid
import os

DATA_FILE = 'data/data.csv'

def _ensure_file_exists():
    directory = os.path.dirname(DATA_FILE)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=['id', 'date', 'eggs', 'food_cost'])
        df.to_csv(DATA_FILE, index=False)

def get_all_records():
    _ensure_file_exists()
    try:
        df = pd.read_csv(DATA_FILE)
        # Sort by date descending
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date', ascending=False)
        # Convert date back to string for display if needed or keep as object
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')
        return df.to_dict('records')
    except pd.errors.EmptyDataError:
        return []

def add_record(date, eggs, food_cost):
    _ensure_file_exists()
    new_record = {
        'id': str(uuid.uuid4()),
        'date': date,
        'eggs': int(eggs),
        'food_cost': float(food_cost)
    }
    df = pd.DataFrame([new_record])
    # Append to CSV
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
        return record.iloc[0].to_dict()
    return None

def update_record(record_id, date, eggs, food_cost):
    _ensure_file_exists()
    df = pd.read_csv(DATA_FILE)
    if record_id in df['id'].values:
        df.loc[df['id'] == record_id, ['date', 'eggs', 'food_cost']] = [date, int(eggs), float(food_cost)]
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
            return {
                'avg_eggs_day': 0,
                'avg_eggs_month': 0,
                'avg_eggs_year': 0,
                'avg_cost_month': 0,
                'total_eggs': 0,
                'total_cost': 0
            }

        df['date'] = pd.to_datetime(df['date'])

        # Overall Stats
        total_eggs = df['eggs'].sum()
        total_cost = df['food_cost'].sum()
        days_recorded = df['date'].nunique()
        avg_eggs_day = total_eggs / days_recorded if days_recorded > 0 else 0

        # Monthly Stats
        df['month'] = df['date'].dt.to_period('M')
        monthly_stats = df.groupby('month').agg({'eggs': 'sum', 'food_cost': 'sum'})
        avg_eggs_month = monthly_stats['eggs'].mean() if not monthly_stats.empty else 0
        avg_cost_month = monthly_stats['food_cost'].mean() if not monthly_stats.empty else 0

        # Yearly Stats
        df['year'] = df['date'].dt.to_period('Y')
        yearly_stats = df.groupby('year').agg({'eggs': 'sum'})
        avg_eggs_year = yearly_stats['eggs'].mean() if not yearly_stats.empty else 0

        return {
            'avg_eggs_day': round(avg_eggs_day, 2),
            'avg_eggs_month': round(avg_eggs_month, 2),
            'avg_eggs_year': round(avg_eggs_year, 2),
            'avg_cost_month': round(avg_cost_month, 2),
            'total_eggs': int(total_eggs),
            'total_cost': round(total_cost, 2)
        }
    except Exception as e:
        print(f"Error calculating stats: {e}")
        return {
            'avg_eggs_day': 0,
            'avg_eggs_month': 0,
            'avg_eggs_year': 0,
            'avg_cost_month': 0,
            'total_eggs': 0,
            'total_cost': 0
        }
