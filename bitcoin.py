import sys
import requests

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit('Error')

try:
    request = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=8a249a07b7da40aa5acc141f499a34db274171bfe8bb199b639a921ca021b99f')
except requests.RequestException:
    sys.exit('Error')

content = request.json()

price = content['data']['priceUsd']
price = float(price)

price = price * n
print(f'${price:,.4f}')
