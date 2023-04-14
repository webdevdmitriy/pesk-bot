from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton("/котик")

kb_other = ReplyKeyboardMarkup(resize_keyboard=True)

kb_other.row(b1)
