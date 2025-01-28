import random
import time
import sqlite3

def generate_data():
    """
    Simulate mining operations and store in SQLite database.
    """
    conn = sqlite3.connect('database/mining.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mining_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ore_extracted INTEGER,
        truck_load INTEGER,
        machine_status TEXT
    )
    """)

    while True:
        # Generate random data
        ore_extracted = random.randint(50, 100)  # in tons
        truck_load = random.randint(20, 50)     # in tons
        machine_status = random.choice(['Running', 'Idle', 'Maintenance'])

        # Insert data into the database
        cursor.execute("""
        INSERT INTO mining_data (timestamp, ore_extracted, truck_load, machine_status)
        VALUES (datetime('now'), ?, ?, ?)
        """, (ore_extracted, truck_load, machine_status))

        conn.commit()
        print(f"Data Generated: {ore_extracted} tons, Truck: {truck_load} tons, Status: {machine_status}")
        
        time.sleep(2)  # Simulate real-time data generation

if __name__ == "__main__":
    generate_data()
