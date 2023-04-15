from aiogram.utils import executor
from create_bot import dp, bot
from handlers import client
from handlers import admin
from menu import set_main_menu
import requests

from aiogram import Bot, Dispatcher

# dp: Dispatcher = Dispatcher()


# dp.startup.register(set_main_menu)

response = requests.get("https://api.thecatapi.com/v1/breeds")
json = response.json()
# print('breeds', json)

for breed in json:
    print(breed['name'])


async def on_startup(_):
    await set_main_menu(bot)
    print("Бот вышел в онлайн")


client.register_handlers_client(dp)
admin.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
