#Functions module
import requests
import asyncio

#Constants
binance_api_url = "https://api.binance.com/api/v3"
exchange_info = requests.get(f"{binance_api_url}/exchangeInfo").json()


#Getting last price of {symbol} currency
def get_current_price(currency):
    url = f"{binance_api_url}/ticker/price?symbol={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        currenciy_pair = data['symbol']
        price = round(float(data['price']),2)
        text_answer = f"{currenciy_pair} price is {price}"
        return text_answer
    else:
        text_error = f"Ошибка при запросе данных: {response.status_code}"
        return text_error

#Getting 24 volume of {symbol} currency
def get_currency_day_volume(currency):
    url = f"{binance_api_url}/ticker/24hr?symbol={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        volume = float(data['quoteVolume'])
        formated_volume = round(volume / 1000000,2)
        text_answer = f"24-часовой объем торгов по {currency}: {formated_volume} миллионов $ США"
        return text_answer
    else:
        text_error = f"Ошибка при запросе данных: {response.status_code}"
        return text_error

#Getting of list with USDT pairs
def get_usdt_pairs():
    usdt_pairs = []
    url = f'{binance_api_url}/exchangeInfo'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for symbol_info in data['symbols']:
            symbol = symbol_info['symbol']
            if 'USDT' in symbol:
                usdt_pairs.append(symbol)
        return usdt_pairs
    else:
        print("Ошибка при получении данных")


#getting liquid instruments with symbols and 24h trading volume
def get_liquidity_instruments(symbols, volume):
    liquid_pairs = []
    url = f"{binance_api_url}/ticker/24hr"
    response = requests.get(url)
    ticker_info = response.json()

    for item in ticker_info:
        symbol = item['symbol']
        daily_volume = float(item['quoteVolume'])
        if daily_volume > volume and any(symbol in pair for pair in symbols):
            liquid_pairs.append(symbol)
    return print(liquid_pairs)
    


#Cheking of function
#get_current_price('BTCUSDT')
#get_currency_day_volume('BTCUSDT')
#get_liquidity_instruments(get_usdt_pairs(),100000000)