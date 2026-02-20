from flask import Flask, render_template, request, redirect, url_for, session
from data_handler import get_statistics, add_record, get_all_records, get_record, update_record, delete_record
import os
from translations import TRANSLATIONS

app = Flask(__name__)
# Lokaler Key (Sicherheit für lokale Instanz ausreichend)
app.secret_key = 'dev_key_123'

@app.before_request
def before_request():
    if 'language' not in session:
        session['language'] = 'de'

@app.context_processor
def inject_language():
    def t(key):
        lang = session.get('language', 'de')
        return TRANSLATIONS.get(lang, {}).get(key, key)
    return dict(language=session.get('language', 'de'), t=t)

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in TRANSLATIONS:
        session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    stats = get_statistics()
    records = get_all_records()[:10]
    return render_template('index.html', stats=stats, records=records)

@app.route('/add', methods=['POST'])
def add():
    record_type = request.form.get('type')
    date = request.form.get('date')
    amount = request.form.get('amount')
    cost = request.form.get('cost')
    note = request.form.get('note', '')

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
    existing_record = get_record(id)
    
    if not existing_record:
        return redirect(url_for('records'))

    record_type = request.form.get('type', existing_record.get('type'))
    amount = request.form.get('amount', 0)
    cost = request.form.get('cost', 0.0)
    note = request.form.get('note', '')

    update_record(id, date, amount, cost, note, record_type)
    return redirect(url_for('records'))

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    delete_record(id)
    return redirect(url_for('records'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
