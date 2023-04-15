from aiogram import types
from create_bot import dp, bot
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import  kb_breed, kb_cat
import requests



catApi = 'live_IkAb7tMnL1hD4Vhme24oXQcIbNjqvoClEWTp2w02sBuj6okCXydSmwzz1tUup6rg'


class FSMAdmin(StatesGroup):
    breed = State()
    category = State()

# @dp.message.handler(commands='Загрузить', state= None)
async def cm_start(message: types.Message):
    await FSMAdmin.breed.set()
    await message.answer('Выбери породу котика', reply_markup=kb_breed)

async def get_start(callback: types.CallbackQuery, state:FSMContext):
    # print('callback', callback)
   
    # res = callback.split(' ')[0]
    # await callback.answer(res)
    res = callback.data.split(' ')[1]
    async with state.proxy() as data:
        data['breed'] = res
    await FSMAdmin.next()
    await callback.message.answer("Введите вид котика", reply_markup=kb_cat)


async def load_cat(callback: types.CallbackQuery, state:FSMContext):
    res = callback.data.split(' ')[1]
    async with state.proxy() as data:
        data['category'] = res
    async with state.proxy() as data:
        await callback.message.reply(str(data))
        
    data= await state.get_data()
    print('data', data)

    response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit=10&breed_ids={data['breed']}&category_ids={data['category']}&api_key={catApi}")
    print('response', response)
    json = response.json()
    # await bot.send_photo(
    #     message.chat.id,
    #     photo=json[0]["url"],
    # )
    print(json)
    await callback.message.answer_photo(photo=json[0]["url"])
  

#   https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=REPLACE_ME
    await state.finish()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=["Загрузить"])
    dp.register_callback_query_handler(get_start,Text(startswith='breed'), state=FSMAdmin.breed)
    dp.register_callback_query_handler(load_cat,Text(startswith='cat'), state=FSMAdmin.category)

