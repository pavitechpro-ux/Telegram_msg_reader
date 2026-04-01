from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/signals")
def get_signals():
    conn = sqlite3.connect("signals.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM signals ORDER BY id DESC")
    rows = cursor.fetchall()

    return {"data": rows}

@router.get("/stats")
def get_stats():
    conn = sqlite3.connect("signals.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM signals")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM signals WHERE result='WIN'")
    wins = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM signals WHERE result='LOSS'")
    losses = cursor.fetchone()[0]

    accuracy = (wins / total * 100) if total > 0 else 0

    return {
        "total": total,
        "wins": wins,
        "losses": losses,
        "accuracy": round(accuracy, 2)
    }