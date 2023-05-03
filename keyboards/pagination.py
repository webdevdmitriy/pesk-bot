from aiogram import Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData
from create_bot import dp, bot

from typing import Collection


navigation = CallbackData("navigation", "action", "direction")


class Pagination:
    def __init__(self, buttons: Collection[InlineKeyboardButton], buttons_on_page: int = 3) -> None:
        self.__buttons = buttons
        self.__buttons_on_page = buttons_on_page
        self.__current_page = 0

    async def update_kb(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup()
        from_ = self.__current_page * self.__buttons_on_page
        to_ = (self.__current_page + 1) * self.__buttons_on_page

        prev_button = InlineKeyboardButton("Назад",
                                           callback_data=navigation.new(action="navigate", direction="previous"))
        next_button = InlineKeyboardButton("Вперед",
                                           callback_data=navigation.new(action="navigate", direction="next"))

        for button in self.__buttons[from_:to_]:
            markup.row(button)

        if from_ <= 0:
            return markup.row(next_button)
        elif to_ >= len(self.__buttons):
            return markup.row(prev_button)
        return markup.row(prev_button, next_button)

    async def on_next(self) -> None:
        self.__current_page += 1

    async def on_prev(self) -> None:
        self.__current_page -= 1


def start_buttons(amount: int = 15) -> Collection[InlineKeyboardButton]:
    return [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(amount)]


# pagination = Pagination(start_buttons(15), 2)


# @dp.message_handler(commands=["start"])
# async def on_start(message: Message) -> None:
#     await message.answer("MENU", reply_markup=await pagination.update_kb())


