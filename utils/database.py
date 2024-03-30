import disnake
import aiosqlite
from disnake.ext import commands


# Создание базы данных и таблицы
async def create_db():
    async with aiosqlite.connect('warnings.db') as db:
        await db.execute("CREATE TABLE IF NOT EXISTS warnings (user_id INTEGER PRIMARY KEY, num_warnings INTEGER)")
        await db.commit()

# Функция для получения количества предупреждений пользователя
async def get_warnings(user_id):
    async with aiosqlite.connect('warnings.db') as db:
        cursor = await db.execute("SELECT num_warnings FROM warnings WHERE user_id = ?", (user_id,))
        row = await cursor.fetchone()
        return row[0] if row else 0

# Функция для добавления предупреждения пользователю
async def add_warning(user_id):
    async with aiosqlite.connect('warnings.db') as db:
        current_warnings = await get_warnings(user_id)
        await db.execute("INSERT OR REPLACE INTO warnings (user_id, num_warnings) VALUES (?, ?)", (user_id, current_warnings + 1))
        await db.commit()
