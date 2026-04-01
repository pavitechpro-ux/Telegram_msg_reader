from fastapi import WebSocket

clients = []

async def connect(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

def disconnect(websocket: WebSocket):
    clients.remove(websocket)

async def broadcast(message: str):
    for client in clients:
        await client.send_text(message)