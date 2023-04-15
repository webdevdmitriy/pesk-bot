from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import requests



response = requests.get("https://api.thecatapi.com/v1/breeds")
json = response.json()
# print('breeds', json)




# b1 = KeyboardButton("/admin")
# b2 = KeyboardButton("/other")

# kb_breed = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_breed = InlineKeyboardMarkup()

# kb_breed.row(b1, b2)


for breed in json:
    print(breed['name'])
    kb_breed.add(InlineKeyboardButton(breed['name'], callback_data=f"breed {breed['id']}"))


response = requests.get("https://api.thecatapi.com/v1/categories")
json = response.json()
# print('breeds', json)

kb_cat = InlineKeyboardMarkup()

for cat in json:
    print(breed['name'])
    kb_cat.add(InlineKeyboardButton(cat['name'], callback_data=f"cat {cat['id']}"))