from aiogram import types
from create_bot import dp, bot
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import  kb_breed, kb_cat, kb_cat_start, kb_cat_count, pagination
from aiogram.types import MediaGroup, InputFile
import requests


catApi = 'live_IkAb7tMnL1hD4Vhme24oXQcIbNjqvoClEWTp2w02sBuj6okCXydSmwzz1tUup6rg'

class FSMAdmin(StatesGroup):
    breed = State()
    category = State()
    count = State()

async def cat_start(message: types.Message):
    await message.answer('Выбери', reply_markup=kb_cat_start)

async def load_cat(callback: types.CallbackQuery):
     res = callback.data.split(' ')[1]
     print(res)
     if res=='breed':
        await FSMAdmin.breed.set()
        await callback.message.answer("Выберите породу котика", reply_markup=kb_breed)
        # await callback.message.answer("Выберите породу котика", reply_markup=await pagination.update_kb())
     if res=='category':
        await FSMAdmin.category.set()
        await callback.message.answer("Выберите категорию", reply_markup=kb_cat)
     if res=='random':
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        json = response.json()
        await callback.message.answer_photo(photo=json[0]["url"], reply_markup=kb_cat_start)
         
async def cat_breed(callback: types.CallbackQuery, state: FSMContext):
    res = callback.data.split(' ')[1]
    async with state.proxy() as data:
        data['breed'] = res
    await FSMAdmin.count.set()
    await callback.message.answer('Выбери кол-во котиков', reply_markup=kb_cat_count)


async def cat_category(callback: types.CallbackQuery, state: FSMContext):
    res = callback.data.split(' ')[1]
    async with state.proxy() as data:
        data['category'] = res
    await FSMAdmin.count.set()
    await callback.message.answer('Выбери кол-во котиков', reply_markup=kb_cat_count)
  
    
async def cat_result(callback: types.CallbackQuery, state: FSMContext):
    res = callback.data.split(' ')[1]
    async with state.proxy() as data:
        data['count'] = res
    data= await state.get_data()
    print('data', data)

    response = None

    if 'breed' in data:
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit={data['count']}&breed_ids={data['breed']}&api_key={catApi}") 
    if 'category' in data:
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit={data['count']}&category_ids={data['category']}&api_key={catApi}") 

    print('response', response)
    json = response.json()

    media = MediaGroup()
    for item in json:
        media.attach_photo(item["url"], 'Превосходная фотография')
        # await callback.message.answer_photo(photo=item["url"])
    await callback.message.answer_media_group(media=media)
    await callback.message.answer('Выбери', reply_markup=kb_cat_start)
    await state.finish()






def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cat_start, commands=["котик"])
    dp.register_callback_query_handler(load_cat,Text(startswith='cat_start'))
    dp.register_callback_query_handler(cat_breed,Text(startswith='breed'), state=FSMAdmin.breed)
    dp.register_callback_query_handler(cat_category,Text(startswith='cat'), state=FSMAdmin.category)
    dp.register_callback_query_handler(cat_result,Text(startswith='cat_count'), state=FSMAdmin.count)


