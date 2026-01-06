from flask import Flask, render_template, request, redirect, url_for
from data_handler import get_statistics, add_record, get_all_records, get_record, update_record, delete_record
import os

app = Flask(__name__)

@app.route('/')
def index():
    stats = get_statistics()
    # Also get recent 5 records for the dashboard
    records = get_all_records()[:5]
    return render_template('index.html', stats=stats, records=records)

@app.route('/add', methods=['POST'])
def add():
    date = request.form.get('date')
    eggs = request.form.get('eggs')
    food_cost = request.form.get('food_cost')

    if date and eggs and food_cost:
        add_record(date, eggs, food_cost)

    return redirect(url_for('index'))

@app.route('/records')
def records():
    all_records = get_all_records()
    return render_template('records.html', records=all_records)

@app.route('/edit/<id>')
def edit(id):
    record = get_record(id)
    if record:
        return render_template('edit.html', record=record)
    return redirect(url_for('records'))

@app.route('/update/<id>', methods=['POST'])
def update(id):
    date = request.form.get('date')
    eggs = request.form.get('eggs')
    food_cost = request.form.get('food_cost')

    if date and eggs and food_cost:
        update_record(id, date, eggs, food_cost)

    return redirect(url_for('records'))

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    delete_record(id)
    return redirect(url_for('records'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
