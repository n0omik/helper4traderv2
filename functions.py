#Functions module
import requests

#test_currency


def get_current_price(currency)
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={currency}"
    data = requests.get(key)
    data = data.json()
    price = f"{data['symbol']} price is {data['price']}"
    return price

def get_current_volume(currency):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        volume = float(data['volume'])
        print(f"24-часовой объем торгов по {symbol}: {volume}")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

get_current_price('BTCUSDT')
get_current_volume('BTCUSDT')