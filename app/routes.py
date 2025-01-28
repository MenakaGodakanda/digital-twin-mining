from flask import Blueprint, render_template, jsonify
import sqlite3

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/data')
def api_data():
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mining_data ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)
