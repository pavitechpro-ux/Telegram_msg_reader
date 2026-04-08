# import MetaTrader5 as mt5

# def connect_mt5():
#     if not mt5.initialize():
#         print("❌ MT5 initialization failed")
#         return False

#     login = 24683141
#     password = "Fa5Ja@#N"
#     server = "VantageInternational-Demo"

#     # login = 463217020
#     # password = "Qwertyuiop@1"
#     # server = "Exness-MT5Trial17"

#     if not mt5.login(login, password=password, server=server):
#         print("❌ MT5 login failed")
#         return False

#     print("✅ Connected to MT5")
#     return True

# def place_trade(signal):
#     symbol = signal["symbol"]
#     lot = 0.01

#     if not mt5.symbol_select(symbol, True):
#         print("❌ Symbol not found")
#         return

#     tick = mt5.symbol_info_tick(symbol)
#     if tick is None:
#         print("❌ Could not get symbol price")
#         return

#     if signal["type"] == "BUY":
#         order_type = mt5.ORDER_TYPE_BUY
#         price = tick.ask
#     else:
#         order_type = mt5.ORDER_TYPE_SELL
#         price = tick.bid

#     tp_list = signal.get("tp", [])
#     tp_value = tp_list[0] if tp_list else 0.0
#     sl_value = signal.get("sl") or 0.0

#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": lot,
#         "type": order_type,
#         "price": price,
#         "sl": sl_value,
#         "tp": tp_value,
#         "deviation": 10,
#         "magic": 123456,
#         "comment": "AutoTrade",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }

#     result = mt5.order_send(request)
#     print("📊 Trade result:", result)
#     return result





import MetaTrader5 as mt5

def connect_mt5():
    if not mt5.initialize():
        print("❌ MT5 initialization failed")
        print("MT5 last error:", mt5.last_error())
        return False
    
    login = 24683141
    password = "Fa5Ja@#N"
    server = "VantageInternational-Demo"

    # login = 127675829
    # password = "Mt@127675829"
    # server = "Exness-MT5Real7"

    if not mt5.login(login, password=password, server=server):
        print("❌ MT5 login failed")
        print("MT5 last error:", mt5.last_error())
        return False

    print("✅ Connected to MT5")
    return True

def place_trade(signal):
    symbol = signal["symbol"]
    lot = 0.01

    if not mt5.symbol_select(symbol, True):
        print(f"❌ Symbol not found: {symbol}")
        return None

    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"❌ Could not get symbol price: {symbol}")
        return None

    if signal["type"] == "BUY":
        order_type = mt5.ORDER_TYPE_BUY
        price = tick.ask
    else:
        order_type = mt5.ORDER_TYPE_SELL
        price = tick.bid

    tp_list = signal.get("tp", [])
    tp_value = tp_list[0] if tp_list else 0.0
    sl_value = signal.get("sl") or 0.0

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl_value,
        "tp": tp_value,
        "deviation": 10,
        "magic": 123456,
        "comment": "AutoTrade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    print("🚀 Sending MT5 order:", request)
    result = mt5.order_send(request)
    print("📊 Trade result:", result)

    return result