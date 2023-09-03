import random
from mexc_sdk.src.mexc_sdk import Spot


price = 0
symbol = "BTCUSDT"
accounts = [
    {
        'access': '*',
        'private': '*',
        'side': 'BUY',
        'order_type': 'MARKET'
    },
    {
        'access': '*',
        'private': '*',
        'side': 'SELL',
        'order_type': 'MARKET'
    }
]

while True:
    client = Spot(api_key=accounts[0]['access'], api_secret=accounts[0]['private'])
    if len(client.trades(symbol=symbol, options={"limit": 5})) > 0:
        price = float(client.trades(symbol=symbol, options={"limit": 5})[0]['price'])
    quantity = random.randint(50, 50000)
    for account in accounts:
        client = Spot(api_key=account['access'], api_secret=account['private'])
        res = client.new_order_test(symbol=symbol, side=account['side'], order_type=account['order_type'], options={"quantity": quantity, "price": price})
