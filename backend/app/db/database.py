import sqlite3
import json

conn = sqlite3.connect("signals.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    symbol TEXT,
    entry REAL,
    sl REAL,
    tp TEXT,
    executed INTEGER DEFAULT 0
)
""")
conn.commit()

def save_signal(data):
    cursor.execute(
        "INSERT INTO signals (type, symbol, entry, sl, tp, executed) VALUES (?, ?, ?, ?, ?, ?)",
        (
            data.get("type"),
            data.get("symbol"),
            data.get("entry"),
            data.get("sl"),
            json.dumps(data.get("tp", [])),
            0
        )
    )
    conn.commit()