# from app.services.validator import validate_signal

# from app.services.trade_executor_mt5 import place_trade

# from telethon import TelegramClient, events
# from app.parser.signal_parser import parse_signal
# from app.db.database import save_signal
# from app.core.connection_manager import broadcast
# import json


# api_id = 39732579
# api_hash = "722ab7a8bc27a6365cc81a60a65f5dd8"


# # 🔹 Target group name
# TARGET_GROUP_NAME = "Autobotsignal"

# # 🔹 Create client
# client = TelegramClient("session", api_id, api_hash)


# @client.on(events.NewMessage)
# async def handler(event):
#     chat = await event.get_chat()

#     # ❗ Ignore messages without title (like private chats)
#     if not hasattr(chat, "title"):
#         return

#     # 🔥 FILTER USING GROUP NAME
#     if TARGET_GROUP_NAME.lower() not in chat.title.lower():
#         return

#     msg = event.message.text

#     print(f"\n📩 {chat.title}: {msg}")

#     # 🔹 Parse signal
#     parsed = parse_signal(msg)

#     # if parsed:
#     #     save_signal(parsed)
#     #     print("✅ Saved:", parsed)

#     #     # 🔥 Send to frontend via WebSocket
#     #     await broadcast(json.dumps(parsed))

#     if parsed:
#         save_signal(parsed)
#         print("✅ Saved:", parsed)

#     # 🔥 VALIDATE BEFORE TRADE
#     if validate_signal(parsed):
#         place_trade(parsed)

#     await broadcast(json.dumps(parsed))

# # 🔹 Start listener
# async def start_listener():
#     await client.start()
#     print("🚀 Telegram Listener Started (Group Filter Applied)")
#     await client.run_until_disconnected()






from app.services.validator import validate_signal
from telethon import TelegramClient, events
from app.parser.signal_parser import parse_signal
from app.db.database import save_signal
from app.core.connection_manager import broadcast
import json


api_id = 
api_hash = ""

TARGET_GROUP_NAME = "Autobotsignal"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()

    if not hasattr(chat, "title"):
        return

    if TARGET_GROUP_NAME.lower() not in chat.title.lower():
        return

    msg = event.message.text
    print(f"\n📩 {chat.title}: {msg}")

    parsed = parse_signal(msg)

    if not parsed:
        print("❌ Parser returned None")
        return

    print("🧠 Parsed:", parsed)

    if not validate_signal(parsed):
        print("❌ Validation failed, signal not saved")
        return

    save_signal(parsed)
    print("✅ Saved:", parsed)

    await broadcast(json.dumps(parsed))

async def start_listener():
    await client.start()
    print("🚀 Telegram Listener Started (Group Filter Applied)")
    await client.run_until_disconnected()
