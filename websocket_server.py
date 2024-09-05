import asyncio
import websockets
import json
import hmac
import hashlib
import base64
import requests

API_KEY = "28409f4c-5098-4ce6-8962-56036aa16eff"
SECRET_KEY = "CD70A76598BE0E466203BEB52DFB6B2F"
PASSPHRASE = "T@6pighv"
BASE_URL = "https://www.okx.com"

# Sign a message for API authentication
def sign_message(timestamp, method, request_path, body):
    message = timestamp + method + request_path + body
    mac = hmac.new(bytes(SECRET_KEY, 'utf-8'), bytes(message, 'utf-8'), hashlib.sha256)
    return base64.b64encode(mac.digest()).decode('utf-8')

# OKX API for Order-Book updates
def fetch_real_time_data(symbol):
    url = f"{BASE_URL}/api/v5/market/books?instId={symbol}&sz=5"
    response = requests.get(url)
    return response.json()

# Function to handle client connections
async def handle_client(websocket):
    subscribed_symbols = set()
    
    try:
        async for message in websocket:
            data = json.loads(message)
            if data['action'] == 'subscribe':
                symbol = data['symbol']
                subscribed_symbols.add(symbol)
                await websocket.send(f"Subscribed to {symbol}")
                print(f"Client subscribed to {symbol}")

            elif data['action'] == 'unsubscribe':
                symbol = data['symbol']
                if symbol in subscribed_symbols:
                    subscribed_symbols.remove(symbol)
                    await websocket.send(f"Unsubscribed from {symbol}")
                    print(f"Client unsubscribed from {symbol}")

            # Send updates to the client for subscribed symbols
            while subscribed_symbols:
                for symbol in list(subscribed_symbols):
                    try:
                        real_time_data = fetch_real_time_data(symbol)
                        await websocket.send(json.dumps(real_time_data))
                        await asyncio.sleep(5)  # Fetch data every 5 seconds
                    except websockets.ConnectionClosed:
                        print("Connection closed")
                        return

    except websockets.ConnectionClosed:
        print("Connection closed")

# Main function to run the WebSocket server
async def main():
    server = await websockets.serve(handle_client, "localhost", 6789)
    print("WebSocket server started on ws://localhost:6789")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
