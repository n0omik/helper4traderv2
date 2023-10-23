import json 
import requests 
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message

#API TOKEN for telegram bot n0omik
API_TOKEN = '6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

currencies = ["BTCUSDT","ETHUSDT","SOLUSDT"] 
  
# function of printing btc price
def get_crypto_price(currency):
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={currency}"
    data = requests.get(key)
    data = data.json()
    price = f"{data['symbol']} price is {data['price']}"
    return price

#function of btc price
@dp.message_handler(commands=['Bitcoin_price'])
async def btc_price(message: types.Message):
    price_text = get_crypto_price(['BTCUSDT'])
    await message.answer(text=price_text)

@dp.message_handler(commands=['Etherium_price'])
async def eth_price(message: types.Message):
    price_text = get_crypto_price(['ETHUSDT'])
    await message.answer(text=price_text)

@dp.message_handler(commands=['Solana_price'])
async def sol_price(message: types.Message):
    price_text = get_crypto_price(['SOLUSDT'])
    await message.answer(text=price_text)

# Function to handle button clicks
@dp.message_handler(lambda message: message.text in ["/Bitcoin_price", "/Etherium_price", "/Solana_price"])
async def handle_button_click(message: types.Message):
    command = message.text
    if command == "/Bitcoin_price":
        await btc_price(message)
    elif command == "/Etherium_price":
        await eth_price(message)
    elif command == "/Solana_price":
        await sol_price(message)

# Function for the /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="/Bitcoin_price"))
    kb.add(types.KeyboardButton(text="/Etherium_price"))
    kb.add(types.KeyboardButton(text="/Solana_price"))
    await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте, проверка связи!", reply_markup=kb)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)