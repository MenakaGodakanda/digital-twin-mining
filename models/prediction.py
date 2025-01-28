import sqlite3

def calculate_average():
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(ore_extracted) FROM mining_data")
    avg = cursor.fetchone()[0]
    conn.close()
    return avg

def check_downtime():
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM mining_data WHERE machine_status = 'Idle'")
    downtime_count = cursor.fetchone()[0]
    conn.close()
    return downtime_count > 5  # Alert if more than 5 idle records
