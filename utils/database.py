import disnake
import aiosqlite
from disnake.ext import commands


# Создание базы данных и таблицы
async def create_db():
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        warns INTEGER DEFAULT 0,
        guild_id INTEGER
    )''')
        await db.execute('''CREATE TABLE IF NOT EXISTS warns (
            user_id INTEGER,
            warn_id INTEGER PRIMARY KEY AUTOINCREMENT,
            guild_id INTEGER,
            reason TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
    )''')
        await db.commit()


# Функция для добавления нового пользователя
async def add_user(user_id, guild_id):
    async with aiosqlite.connect('users.db') as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id, guild_id, warns) VALUES (?, ?, 0)", (user_id, guild_id))
        await db.commit()

# Функция для добавления предупреждения пользователю
async def add_warn(user_id, guild_id, reason):
    async with aiosqlite.connect('users.db') as db:
        await db.execute("INSERT INTO warns (user_id, guild_id, reason) VALUES (?, ?, ?)", (user_id, guild_id, reason))
        await db.execute("UPDATE users SET warns = warns + 1 WHERE user_id = ? AND guild_id = ?", (user_id, guild_id))
        await db.commit()

# Функция для получения информации о пользователе и его варнах
async def get_user_info(user_id, guild_id):
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE user_id = ? AND guild_id = ?", (user_id, guild_id))
        user_info = await cursor.fetchone()
        cursor = await db.execute("SELECT * FROM warns WHERE user_id = ? AND guild_id = ?", (user_id, guild_id))
        warns = await cursor.fetchall()
        return user_info, warns
