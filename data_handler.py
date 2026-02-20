import pandas as pd
import uuid
import os
from datetime import datetime

DATA_FILE = 'data/data.csv'
_CACHED_DF = None
_LAST_MTIME = 0

def _ensure_file_exists():
    directory = os.path.dirname(DATA_FILE)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=['id', 'date', 'type', 'amount', 'cost', 'note'])
        df.to_csv(DATA_FILE, index=False)

def _get_data():
    global _CACHED_DF, _LAST_MTIME
    _ensure_file_exists()
    try:
        current_mtime = os.path.getmtime(DATA_FILE)
        if _CACHED_DF is not None and current_mtime == _LAST_MTIME:
            return _CACHED_DF.copy()

        # Explizite Typ-Definition beim Einlesen, um den float64-Fehler zu verhindern
        df = pd.read_csv(DATA_FILE)
        
        if not df.empty:
            df['date'] = pd.to_datetime(df['date'])
            # WICHTIG: Notiz-Feld immer als Text (String) behandeln
            df['note'] = df['note'].fillna('').astype(str)
            df['id'] = df['id'].astype(str)
            df['type'] = df['type'].astype(str)
            # Zahlen-Spalten absichern
            df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
            df['cost'] = pd.to_numeric(df['cost'], errors='coerce').fillna(0.0)
        else:
            df = pd.DataFrame(columns=['id', 'date', 'type', 'amount', 'cost', 'note'])
            df = df.astype({'id': str, 'type': str, 'note': str, 'amount': float, 'cost': float})

        _CACHED_DF = df
        _LAST_MTIME = current_mtime
        return df.copy()
    except (pd.errors.EmptyDataError, FileNotFoundError):
        return pd.DataFrame(columns=['id', 'date', 'type', 'amount', 'cost', 'note'])

def get_all_records():
    df = _get_data()
    if df.empty: return []
    
    df = df.sort_values(by='date', ascending=False)
    df['display_date'] = df['date'].dt.strftime('%d/%m/%Y')
    # Raw date für HTML-Input
    df['raw_date'] = df['date'].dt.strftime('%Y-%m-%d')
    
    records = df.to_dict('records')
    type_map = {'egg': 'Eier', 'food': 'Futter', 'chicken': 'Hühner'}

    for r in records:
        r['date'] = r['display_date']
        r['type_display'] = type_map.get(r['type'], r['type'])
    return records

def add_record(date, record_type, amount=0, cost=0.0, note=""):
    _ensure_file_exists()
    try:
        if record_type == 'food':
            amount_val = float(amount) if amount else 0.0
        else:
            amount_val = int(float(amount)) if amount else 0
        cost_val = float(cost) if cost else 0.0
    except (ValueError, TypeError):
        amount_val, cost_val = 0, 0.0

    new_record = {
        'id': str(uuid.uuid4()), 
        'date': date, 
        'type': record_type,
        'amount': amount_val, 
        'cost': cost_val, 
        'note': str(note) if note else ""
    }
    
    df_new = pd.DataFrame([new_record])
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        df_new.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df_new.to_csv(DATA_FILE, index=False)
    
    global _LAST_MTIME
    _LAST_MTIME = 0 # Cache zurücksetzen
    return new_record['id']

def get_record(record_id):
    df = _get_data()
    record = df[df['id'] == record_id].copy()
    if not record.empty:
        record['date'] = record['date'].dt.strftime('%Y-%m-%d')
        return record.fillna('').iloc[0].to_dict()
    return None

def update_record(record_id, date, amount, cost, note, record_type=None):
    df = _get_data()
    if record_id in df['id'].values:
        idx = df.index[df['id'] == record_id][0]
        new_type = record_type if record_type else df.at[idx, 'type']

        try:
            if new_type == 'food':
                amount_val = float(amount) if amount else 0.0
            else:
                amount_val = int(float(amount)) if amount else 0
            cost_val = 0.0 if new_type == 'egg' else (float(cost) if cost else 0.0)
        except (ValueError, TypeError):
            amount_val, cost_val = df.at[idx, 'amount'], df.at[idx, 'cost']

        # Update der Werte
        df.loc[idx, 'date'] = pd.to_datetime(date)
        df.loc[idx, 'type'] = str(new_type)
        df.loc[idx, 'amount'] = amount_val
        df.loc[idx, 'cost'] = cost_val
        df.loc[idx, 'note'] = str(note)

        df.to_csv(DATA_FILE, index=False)
        global _LAST_MTIME
        _LAST_MTIME = 0
        return True
    return False

def delete_record(record_id):
    df = _get_data()
    if record_id in df['id'].values:
        df = df[df['id'] != record_id]
        df.to_csv(DATA_FILE, index=False)
        global _LAST_MTIME
        _LAST_MTIME = 0
        return True
    return False

def get_statistics():
    try:
        df = _get_data()
        if df.empty: return _empty_stats()
        
        eggs_df = df[df['type'] == 'egg']
        food_df = df[df['type'] == 'food']
        chicken_df = df[df['type'] == 'chicken']

        total_eggs = eggs_df['amount'].sum()
        current_chickens = chicken_df['amount'].sum()
        
        start_date = df['date'].min()
        end_date = max(pd.Timestamp.now().normalize(), df['date'].max())
        days = (end_date - start_date).days + 1
        
        total_food_cost = food_df['cost'].sum()
        total_chicken_cost = chicken_df['cost'].sum()

        return {
            'avg_eggs_day': round(total_eggs / days if days > 0 else 0, 2),
            'current_chickens': int(current_chickens),
            'cost_per_egg': round((total_food_cost + total_chicken_cost) / total_eggs if total_eggs > 0 else 0, 2),
            'total_eggs': int(total_eggs),
            'total_food_cost': round(total_food_cost, 2),
            'total_chicken_cost': round(total_chicken_cost, 2),
            'avg_food_cost_month': round(total_food_cost / (max(1, days/30)), 2)
        }
    except Exception:
        return _empty_stats()

def _empty_stats():
    return {k: 0 for k in ['avg_eggs_day', 'current_chickens', 'cost_per_egg', 'total_eggs', 'total_food_cost', 'total_chicken_cost', 'avg_food_cost_month']}
