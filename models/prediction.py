import sqlite3

def calculate_average():
    """
    Calculate the average ore extraction from the database.
    """
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(ore_extracted) FROM mining_data")
    avg = cursor.fetchone()[0]
    conn.close()
    return round(avg, 2) if avg else 0

def check_downtime():
    """
    Check if the machine has been idle for more than 5 consecutive records.
    """
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT machine_status FROM mining_data 
        ORDER BY timestamp DESC LIMIT 10
    """)
    statuses = [row[0] for row in cursor.fetchall()]
    conn.close()
    return statuses.count('Idle') >= 5  # Alert if 5 or more consecutive 'Idle'
