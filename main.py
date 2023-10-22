import json 
import requests 
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message


currencies = ["BTCUSDT"] 
  
# function of printing btc price
def currencies_price(currencies):
    for currency in currencies:
      key = f"https://api.binance.com/api/v3/ticker/price?symbol={currency}"
      data = requests.get(key) 
      data = data.json() 
      print(f"{data['symbol']} price is {data['price']}") 

#API TOKEN for telegram bot n0omik
API_TOKEN = '6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#function of start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="/Bitcoin_price"),
           types.KeyboardButton(text="А это?")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте", reply_markup=keyboard)

#function of btc price
@dp.message_handler(commands=['Bitcoin_price'])
async def btc_price(message: types.Message):
   await message.answer(text=currencies_price(currencies))
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)