from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from create_bot import bot
from bot_telegram import create_profile



async def set_main_menu(bot: bot):
    # Создаем список с командами и их описанием для кнопки menu
    # create_profile()
    main_menu_commands = [
        BotCommand(command="/admin", description="Справочная информация"),
        BotCommand(command="/other", description="Всякое разное"),
    ]
    await bot.set_my_commands(main_menu_commands)
