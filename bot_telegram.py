from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# улавливает любые сооющения, которые приходят боту
@dp.message_handler()
async def echo_send(message: types.message):
    await message.answer(message.text)


executor.start_polling(dp,skip_updates=True)