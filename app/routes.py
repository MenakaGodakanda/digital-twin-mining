from flask import Blueprint, render_template, jsonify
import sqlite3
from models.prediction import calculate_average, check_downtime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/data')
def api_data():
    # Fetch the latest 10 data records
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mining_data ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    
    # Calculate average and downtime alert
    avg_ore_extraction = calculate_average()
    downtime_alert = check_downtime()

    return jsonify({
        "data": data,
        "average_ore_extraction": avg_ore_extraction,
        "downtime_alert": downtime_alert
    })
