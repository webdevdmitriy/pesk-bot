from aiogram.utils import executor
from create_bot import dp, bot
from handlers import client
from handlers import cats
from menu import set_main_menu
import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, name TEXT, photo TEXT)")
    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetck
    if not user:
        cur.execute('INSERT INTO profile values(?,?,?)', (user_id,))
        db.commit()
    # INSERT INTO profile VALUES()

async def on_startup(_):
    await db_start()
    await set_main_menu(bot)
    print("Бот вышел в онлайн")

# async

client.register_handlers_client(dp)
cats.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

