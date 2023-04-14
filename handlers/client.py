from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_admin, kb_other
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand


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


async def send_photo(message: types.message):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json = response.json()
    await bot.send_photo(
        message.chat.id,
        # photo="http://chudo-prirody.com/uploads/posts/2021-08/1628647490_127-p-udivlennii-kot-foto-133.jpg",
        photo=json[0]["url"],
    )


# улавливает любые сооющения, которые приходят боту
# @dp.message_handler()
# async def echo_send(message: types.message):
#     await message.answer(message.text)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(wifi_password_command, commands=["Wi-Fi"])
    dp.register_message_handler(send_photo, commands=["котик"])
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(admins_command, commands=["admin"])
    dp.register_message_handler(other_command, commands=["other"])
    dp.register_message_handler(server_command, commands=["Сервер"])

    # dp.register_message_handler(echo_send)
