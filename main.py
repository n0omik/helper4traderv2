from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте")

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)