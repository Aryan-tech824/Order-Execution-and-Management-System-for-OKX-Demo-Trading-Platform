import asyncio
import websockets
from websockets.asyncio.client import connect
import json

async def subscribe_to_symbol():
    uri = "ws://localhost:6789"  # WebSocket server URL

    symbol = input("Enter the symbol to subscribe to (e.g., BTC-USDT): ")

    async with websockets.connect(uri) as websocket:
        # Send message to the server
        subscribe_message = json.dumps({"action": "subscribe", "symbol": symbol})
        await websocket.send(subscribe_message)
        print(f"Subscribed to {symbol}")

        # Listen from the server
        while True:
            response = await websocket.recv()
            print(f"Received update: {response}")

if __name__ == "__main__":
    asyncio.run(subscribe_to_symbol())
