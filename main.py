import json 
import requests 
from aiogram import Bot, Dispatcher, executor, types

key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# Making list for multiple crypto's 
currencies = ["BTCUSDT"] 

  
# running loop to print all crypto prices
def currencies_price(currencies):
   j = 0
   for i in currencies: 
    # completing API for request 
    url = key+currencies[j]   
    data = requests.get(url) 
    data = data.json() 
    j = j+1
    print(f"{data['symbol']} price is {data['price']}") 


API_TOKEN = '6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте")

@dp.message_handler(commands=['Bitcoin_price'])
async def echo(message: types.Message):
   await message.answer(currencies_price)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)