import sqlite3
import json
import MetaTrader5 as mt5
from app.services.trade_executor_mt5 import place_trade

DB_PATH = "signals.db"

def check_entry_and_execute():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, type, symbol, entry, sl, tp, executed
        FROM signals
        WHERE executed = 0
    """)
    rows = cursor.fetchall()

    for row in rows:
        signal_id, signal_type, symbol, entry, sl, tp_json, executed = row

        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            print(f"❌ No tick data for {symbol}")
            continue

        current_price = tick.ask if signal_type == "BUY" else tick.bid
        tp_list = json.loads(tp_json) if tp_json else []

        print(f"👀 Watching {symbol} | type={signal_type} | entry={entry} | current={current_price}")

        should_execute = False

        if signal_type == "BUY" and current_price >= entry:
            should_execute = True
        elif signal_type == "SELL" and current_price <= entry:
            should_execute = True

        if should_execute:
            signal = {
                "type": signal_type,
                "symbol": symbol,
                "entry": entry,
                "sl": sl,
                "tp": tp_list
            }

            print(f"🎯 Entry hit for signal {signal_id}, placing trade...")
            result = place_trade(signal)

            if result and result.retcode == mt5.TRADE_RETCODE_DONE:
                cursor.execute(
                    "UPDATE signals SET executed = 1 WHERE id = ?",
                    (signal_id,)
                )
                conn.commit()
                print(f"✅ Trade executed and marked done for signal {signal_id}")
            else:
                print(f"❌ Trade not executed for signal {signal_id}")

    conn.close()