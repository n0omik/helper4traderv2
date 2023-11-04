#Functions module
import requests


def get_current_price(currency):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        currenciy_pair = data['symbol']
        price = round(float(data['price']),2)
        print(f"{currenciy_pair} price is {price}")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")


def get_current_volume(currency):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        volume = float(data['quoteVolume'])
        formated_volume = round(volume / 1000000,2)
        print(f"24-часовой объем торгов по {currency}: {formated_volume} миллионов $ США")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

get_current_price('BTCUSDT')
get_current_volume('BTCUSDT')