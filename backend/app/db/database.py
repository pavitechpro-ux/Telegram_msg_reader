import sqlite3

conn = sqlite3.connect("signals.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    symbol TEXT,
    entry REAL
)
""")

def save_signal(data):
    cursor.execute(
        "INSERT INTO signals (type, symbol, entry) VALUES (?, ?, ?)",
        (data.get("type"), data.get("symbol"), data.get("entry"))
    )
    conn.commit()