from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import requests

from aiogram import types
from keyboards.pagination import Pagination
from create_bot import dp, bot
from aiogram.utils.callback_data import CallbackData
from aiogram import Dispatcher

response = requests.get("https://api.thecatapi.com/v1/breeds")
json = response.json()



kb_cat_start =  InlineKeyboardMarkup()
kb_cat_start.add(InlineKeyboardButton('Выбрать породу', callback_data=f"cat_start breed"))
kb_cat_start.add(InlineKeyboardButton('Выбрать категорию', callback_data=f"cat_start category"))
kb_cat_start.add(InlineKeyboardButton('Случайный котик', callback_data=f"cat_start random"))

kb_breed = InlineKeyboardMarkup()

buttons = []
for breed in json:
    kb_breed.add(InlineKeyboardButton(breed['name'], callback_data=f"breed {breed['id']}"))
    # buttons.append(InlineKeyboardButton(breed['name'], callback_data=f"breed {breed['id']}"))


# pagination = Pagination(buttons, 2)
response = requests.get("https://api.thecatapi.com/v1/categories")
json = response.json()

kb_cat = InlineKeyboardMarkup()

for cat in json:
    kb_cat.add(InlineKeyboardButton(cat['name'], callback_data=f"cat {cat['id']}"))


kb_cat_count = InlineKeyboardMarkup()
kb_cat_count.add(InlineKeyboardButton('1', callback_data=f"cat_count 1"))
kb_cat_count.add(InlineKeyboardButton('3', callback_data=f"cat_count 3"))
kb_cat_count.add(InlineKeyboardButton('5', callback_data=f"cat_count 5"))


# navigation = CallbackData("navigation", "action", "direction")
# @dp.callback_query_handler(navigation.filter(action="navigate", direction="next"))
# async def next_(query: CallbackQuery) -> None:
#     await pagination.on_next()
#     await query.message.edit_text("MENU", reply_markup=await pagination.update_kb())


# @dp.callback_query_handler(navigation.filter(action="navigate", direction="previous"))
# async def prev_(query: CallbackQuery) -> None:
#     await pagination.on_prev()
#     await query.message.edit_text("MENU", reply_markup=await pagination.update_kb())
