import requests
import hmac
import hashlib
import base64
import json
from datetime import datetime

API_KEY = "28409f4c-5098-4ce6-8962-56036aa16eff"
SECRET_KEY = "CD70A76598BE0E466203BEB52DFB6B2F"
PASSPHRASE = "T@6pighv"

BASE_URL = "https://www.okx.com"

def get_timestamp(): 
    return datetime.utcnow().isoformat()[:-3] + 'Z'

def sign_message(timestamp, method, request_path, body):
    message = timestamp + method + request_path + body
    mac = hmac.new(bytes(SECRET_KEY, 'utf-8'), bytes(message, 'utf-8'), hashlib.sha256)
    d = mac.digest()
    return base64.b64encode(d).decode('utf-8')

def place_order(symbol, side, price, size, order_type="limit"):
    url = f"{BASE_URL}/api/v5/trade/order"
    timestamp = get_timestamp()
    
    body = json.dumps({
        "instId": symbol,
        "tdMode": "cash",
        "side": side,
        "ordType": order_type,
        "px": price,
        "sz": size
    })

    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": sign_message(timestamp, "POST", "/api/v5/trade/order", body),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json",
        "x-simulated-trading": "1"  # Set to 1 for demo trading
    }

    response = requests.post(url, headers=headers, data=body)
    print(response.json())

def cancel_order(order_id, symbol):
    url = f"{BASE_URL}/api/v5/trade/cancel-order"
    timestamp = get_timestamp()
    
    body = json.dumps({
        "instId": symbol,
        "ordId": order_id
    })

    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": sign_message(timestamp, "POST", "/api/v5/trade/cancel-order", body),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json",
        "x-simulated-trading": "1"  # Set to 1 for simulated trading
    }

    response = requests.post(url, headers=headers, data=body)
    print(response.json())
    
def modify_order(symbol,order_id, size):
    url = f"{BASE_URL}/api/v5/trade/amend-order"
    timestamp = get_timestamp()
    
    body = json.dumps({
        "instId": symbol,
        "newSz": size,
        "ordId": order_id
    })

    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": sign_message(timestamp, "POST", "/api/v5/trade/amend-order", body),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json",
        "x-simulated-trading": "1"  # Set to 1 for simulated trading
    }

    response = requests.post(url, headers=headers, data=body)
    print(response.json())

def get_orderbook(symbol):
    url = f"{BASE_URL}/api/v5/market/books?instId={symbol}&sz=5"  # Adjust 'sz' for depth
    response = requests.get(url)
    print(response.json())

def view_current_positions():
    url = f"{BASE_URL}/api/v5/account/positions"
    timestamp = get_timestamp()

    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": sign_message(timestamp, "GET", "/api/v5/account/positions", ""),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "x-simulated-trading": "1"  # Set to 1 for simulated trading
    }

    response = requests.get(url, headers=headers)
    print(response.json())

if __name__ == "__main__":
    
    # Place an order
    place_order(symbol="BTC-USDT", side="buy", price="3000", size="0.01")

    # Get orderbook
    #get_orderbook(symbol="BTC-USDT")

    # View current positions
    #view_current_positions()

    #cancel_order(order_id="1751622880248037376", symbol="BTC-USDT")
    
    #modify_order(order_id="1751622880248037376", symbol="BTC-USDT",size="0.02")