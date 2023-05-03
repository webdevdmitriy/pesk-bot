from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_admin, kb_other, kb_breed

from aiogram import Dispatcher


async def command_start(message: types.message):
    await message.answer("Привет!", reply_markup=kb_client)


async def wifi_password_command(message: types.message):
    await message.answer("Wi-Fi: PESK\nПароль:PESK%pESk", reply_markup=kb_client)


async def admins_command(message: types.message):
    await message.answer("Администрирование", reply_markup=kb_admin)


async def other_command(message: types.message):
    await message.answer("Что-то еще", reply_markup=kb_other)


async def server_command(message: types.message):
    await message.answer("Как подключиться к серверу:")
    await bot.send_document(
        message.chat.id, open("src\\1. Подключение к серверу.pdf", "rb")
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(wifi_password_command, commands=["Wi-Fi"])
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(admins_command, commands=["admin"])
    dp.register_message_handler(other_command, commands=["other"])
    dp.register_message_handler(server_command, commands=["Сервер"])

