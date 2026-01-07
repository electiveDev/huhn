from flask import Flask, render_template, request, redirect, url_for
from data_handler import get_statistics, add_record, get_all_records, get_record, update_record, delete_record
import os

app = Flask(__name__)

@app.route('/')
def index():
    stats = get_statistics()
    # Get recent records
    records = get_all_records()[:10]
    return render_template('index.html', stats=stats, records=records)

@app.route('/add', methods=['POST'])
def add():
    record_type = request.form.get('type')
    date = request.form.get('date')

    amount = 0
    cost = 0.0
    note = request.form.get('note', '')

    if record_type == 'egg':
        amount = request.form.get('amount')
    elif record_type == 'food':
        amount = request.form.get('amount')
        cost = request.form.get('cost')
    elif record_type == 'chicken':
        amount = request.form.get('amount')
        cost = request.form.get('cost')

    if date and record_type:
        add_record(date, record_type, amount, cost, note)

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
    # Get type from form, defaulting to existing type if somehow missing
    existing_record = get_record(id)
    if not existing_record:
        return redirect(url_for('records'))

    record_type = request.form.get('type', existing_record.get('type'))

    amount = request.form.get('amount', 0)
    cost = request.form.get('cost', 0.0)
    note = request.form.get('note', '')

    if record_type == 'food':
        # For food, amount is weight
        pass
    elif record_type == 'egg':
        # For eggs, cost is not applicable
        cost = 0.0
    elif record_type == 'chicken':
        # For chicken, both are applicable
        pass

    update_record(id, date, amount, cost, note, record_type)
    return redirect(url_for('records'))

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    delete_record(id)
    return redirect(url_for('records'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
