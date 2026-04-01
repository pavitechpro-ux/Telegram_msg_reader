# import ccxt

# # 🔹 Connect to exchange (use testnet first!)
# exchange = ccxt.binance({
#     "apiKey": "h4578x4ENV7mq13m0bmN2VIemuYZZYVUJbyq3Otc9CMiH3DCxCrDSSk2CuP17ued",
#     "secret": "iewsInipm9nBeh1JAcvWrrJnK3K4rPbS9GOZ0PeG3xNqINOZKOL7hobhAJk7PfhF",
#     "enableRateLimit": True,
# })

# def place_trade(signal):
#     try:
#         symbol = signal["symbol"].replace("/", "")
#         side = "buy" if signal["type"] == "BUY" else "sell"

#         amount = 0.001  # 🔥 FIXED SMALL SIZE (SAFE)

#         print(f"🚀 Placing {side} trade for {symbol}")

#         order = exchange.create_market_order(
#             symbol,
#             side,
#             amount
#         )

#         print("✅ Trade executed:", order)
#         return order

#     except Exception as e:
#         print("❌ Trade failed:", str(e))
#         return None