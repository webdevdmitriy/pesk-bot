from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton("/Wi-Fi")
b2 = KeyboardButton("/Сервер")

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_admin.row(b1, b2)
