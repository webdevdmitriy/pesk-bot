from aiogram.utils import executor
from create_bot import dp, bot
from handlers import client
from menu import set_main_menu

from aiogram import Bot, Dispatcher

# dp: Dispatcher = Dispatcher()


# dp.startup.register(set_main_menu)


async def on_startup(_):
    await set_main_menu(bot)
    print("Бот вышел в онлайн")


client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
