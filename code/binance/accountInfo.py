import time
import hmac
import hashlib
import requests

apiKey = 'NPCbBdToyuySIxbFWRWJQXbMpezKk7tNWHJgv0OkM9mzmLEdJcF0NkzNSkpL7NUZ'
secretKey = '2vy4kjfMWkJrBq6TlKzFmBYVVTTcDc139Wzpg6nMxVg0lqac8Dykw4KygeHdDVeZ'

# Funzione per creare una firma HMAC SHA256
def getSignature(queryString):
    return hmac.new(secretKey.encode(), queryString.encode(), hashlib.sha256).hexdigest()

# Funzione per ottenere le informazioni dell'account
def getAccountInfo():
    timestamp = int(time.time() * 1000)
    queryString = f'timestamp={timestamp}'
    signature = getSignature(queryString)

    url = f'https://testnet.binance.vision/api/v3/account?{queryString}&signature={signature}'

    headers = {
        'X-MBX-APIKEY': apiKey
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'HTTP error! status: {response.status_code}')
    else:
        data = response.json()
        print(data)

# Esempio di utilizzo della funzione
getAccountInfo()
