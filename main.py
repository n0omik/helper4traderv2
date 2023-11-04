import json 
import requests 
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message

TOKEN = getenv("6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k")
dp = Dispatcher()

currencies = ["BTCUSDT","ETHUSDT","SOLUSDT"] 
  
# parsing crypto prices
def get_crypto_price(currency):
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={currency}"
    data = requests.get(key)
    data = data.json()
    price = f"{data['symbol']} price is {data['price']}"
    return price

# Function for /Bitcoin_price commandmessege
@dp.message(Command('/Bitcoin_price'))
async def btc_price(message:Message):
    price_text = get_crypto_price('BTCUSDT')
    await message.answer(price_text)

# Function for /Etherium_price command
@dp.message(Command('/Etherium_price'))
async def eth_price(message:Message):
    price_text = get_crypto_price('ETHUSDT')
    await message.answer(price_text)

# Function for /Solana_price command
@dp.message(Command('/Solana_price'))
async def sol_price(message:Message):
    price_text = get_crypto_price('SOLUSDT')
    await message.answer(price_text)

# Function to handle button clicks
@dp.message(lambda message: message in ["/Bitcoin_price", "/Etherium_price", "/Solana_price"])
async def handle_button_click(message:Message):
    command = message.text
    if command == "/Bitcoin_price":
        await btc_price(message)
    elif command == "/Etherium_price":
        await eth_price(message)
    elif command == "/Solana_price":
        await sol_price(message)

# Function for the /start command
@dp.message(Command('start'))
async def send_welcome(message: Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb = types.KeyboardButton(text="/Bitcoin_price")
    kb = types.KeyboardButton(text="/Etherium_price")
    kb = types.KeyboardButton(text="/Solana_price")
    await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте, проверка связи!", reply_markup=kb)

async def main():
    bot = Bot('6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k')
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())