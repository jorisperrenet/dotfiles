import requests
import json

url = 'https://www.bitstamp.net/api/v2/ticker/btcusd/'
res = requests.get(url).json()

price = float(res['last'])
price = format(price, ',.0f')
print(price)
