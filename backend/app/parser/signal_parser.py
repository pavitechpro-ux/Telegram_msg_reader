# import re

# def parse_signal(text):
#     text = text.upper()

#     data = {
#         "type": None,
#         "symbol": None,
#         "entry": None,
#         "tp": [],
#         "sl": None
#     }

#     # 🔹 Detect BUY / SELL (handle typo SEEL)
#     if "BUY" in text:
#         data["type"] = "BUY"
#     elif "SELL" in text or "SEEL" in text:
#         data["type"] = "SELL"

#     # 🔹 Detect symbol (BTC, XAUUSD, etc.)
#     symbol_match = re.search(r"(BTC/USDT|ETH/USDT|XAUUSD|XAGUSD)", text)
#     if symbol_match:
#         data["symbol"] = symbol_match.group()

#     # 🔹 Detect entry (number after BUY/SELL)
#     entry_match = re.search(r"(BUY|SELL|SEEL)\s+\w+\s+(\d+)", text)
#     if entry_match:
#         data["entry"] = float(entry_match.group(2))

#     # 🔹 Detect TP (multiple)
#     tp_matches = re.findall(r"TP\s*(\d+)", text)
#     if tp_matches:
#         data["tp"] = [float(tp) for tp in tp_matches]

#     # 🔹 Detect SL
#     sl_match = re.search(r"SL\s*(\d+)", text)
#     if sl_match:
#         data["sl"] = float(sl_match.group(1))

#     # return only if meaningful
#     if data["type"] and data["symbol"]:
#         return data

#     return None





import re

def parse_signal(text):
    # Clean markdown and normalize
    cleaned_text = text.replace("*", "").replace("✅", " ").strip()
    upper_text = cleaned_text.upper()

    data = {
        "type": None,
        "symbol": None,
        "entry": None,
        "tp": [],
        "sl": None
    }

    # Detect BUY / SELL / SEEL
    if "BUY" in upper_text:
        data["type"] = "BUY"
    elif "SELL" in upper_text or "SEEL" in upper_text:
        data["type"] = "SELL"

    # Detect symbol
    symbol_match = re.search(r"\b(BTC/USDT|ETH/USDT|XAUUSD|XAUUSDm|XAGUSD|EURUSD|GBPUSD|USDJPY)\b", upper_text)
    if symbol_match:
        data["symbol"] = symbol_match.group(1)

    # Detect entry in formats like:
    # XAUUSD BUY 4658
    # BUY XAUUSD 4658
    # XAUUSD SELL 4532
    entry_patterns = [
        r"\b(?:BTC/USDT|ETH/USDT|XAUUSD|XAGUSD|EURUSD|GBPUSD|USDJPY)\s+(BUY|SELL|SEEL)\s+(\d+(?:\.\d+)?)\b",
        r"\b(BUY|SELL|SEEL)\s+(?:BTC/USDT|ETH/USDT|XAUUSD|XAGUSD|EURUSD|GBPUSD|USDJPY)\s+(\d+(?:\.\d+)?)\b",
        r"\bENTRY[:\s]+(\d+(?:\.\d+)?)\b"
    ]

    for pattern in entry_patterns:
        match = re.search(pattern, upper_text)
        if match:
            # ENTRY pattern has only one group
            if "ENTRY" in pattern:
                data["entry"] = float(match.group(1))
            else:
                data["entry"] = float(match.group(2))
            break

    # Detect TP values
    tp_matches = re.findall(r"\bTP[:\s]+(\d+(?:\.\d+)?)\b", upper_text)
    if tp_matches:
        data["tp"] = [float(tp) for tp in tp_matches]

    # Detect SL
    sl_match = re.search(r"\bSL[:\s]+(\d+(?:\.\d+)?)\b", upper_text)
    if sl_match:
        data["sl"] = float(sl_match.group(1))

    # Return only if basic fields exist
    if data["type"] and data["symbol"]:
        return data

    return None