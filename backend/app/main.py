# from fastapi import FastAPI, WebSocket
# from app.api.routes import router
# from app.telegram.listener import start_listener
# from app.core.connection_manager import connect as ws_connect, disconnect
# from app.services.trade_executor_mt5 import connect_mt5
# import asyncio

# app = FastAPI()
# app.include_router(router)

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await ws_connect(websocket)
#     try:
#         while True:
#             await websocket.receive_text()
#     except:
#         disconnect(websocket)

# @app.on_event("startup")
# async def startup_event():
#     connect_mt5()
#     asyncio.create_task(start_listener())






from fastapi import FastAPI, WebSocket
from app.api.routes import router
from app.telegram.listener import start_listener
from app.core.connection_manager import connect as ws_connect, disconnect
from app.services.trade_executor_mt5 import connect_mt5
from app.services.entry_watcher import check_entry_and_execute
import asyncio

app = FastAPI()
app.include_router(router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        disconnect(websocket)

async def signal_monitor():
    while True:
        check_entry_and_execute()
        await asyncio.sleep(2)

@app.on_event("startup")
async def startup_event():
    connect_mt5()
    asyncio.create_task(start_listener())
    asyncio.create_task(signal_monitor())