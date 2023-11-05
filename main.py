import json 
import requests 
import asyncio
import logging
import sys
import functions
import config

from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message


#Setting bot with TOKEN
Bot = Bot(config.TOKEN)
dp = Dispatcher(Bot)

#Getting list of liquid currencies for 24 hours
list_of_liquid_currencies = functions.get_usdt_pairs()
currencies = ["BTCUSDT","ETHUSDT","SOLUSDT"] 

# Messege handler /Bitcoin_price command
@dp.message_handler(commands=['Bitcoin_price'])
async def btc_price(message: types.Message):
    price_text = functions.get_current_price('BTCUSDT')
    await message.answer(price_text)

# Messege handler for /Etherium_price command
@dp.message_handler(commands=['Etherium_price'])
async def eth_price(message: types.Message):
    price_text = functions.get_current_price('ETHUSDT')
    await message.answer(price_text)

# Messege handler for /Solana_price command
@dp.message_handler(commands=['Solana_price'])
async def sol_price(message: types.Message):
    price_text = functions.get_current_price('SOLUSDT')
    await message.answer(price_text)

# Function to handle button clicks
@dp.message_handler(lambda message: message in ["/Bitcoin_price", "/Etherium_price", "/Solana_price"])
async def handle_button_click(message:Message):
    command = message.text
    if command == "/Bitcoin_price":
        await btc_price(message)
    elif command == "/Etherium_price":
        await eth_price(message)
    elif command == "/Solana_price":
        await sol_price(message)

# Function for the /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb = types.KeyboardButton(text="/Bitcoin_price")
    kb = types.KeyboardButton(text="/Etherium_price")
    kb = types.KeyboardButton(text="/Solana_price")
    await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте, проверка связи!", reply_markup=kb)


async def main():
    await dp.start_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())