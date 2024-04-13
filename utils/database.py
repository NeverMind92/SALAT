import aiosqlite

class UsersDataBase:
    def __init__(self):
        self.name = 'dbs/users.db'

    async def setup_database(self):
        async with aiosqlite.connect(self.name) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS warns (
                                user_id INTEGER,
                                server_id INTEGER,
                                num_warns INTEGER,
                                PRIMARY KEY (user_id, server_id)
                            )''')
            await db.commit()

    async def warn_user(self, user_id, server_id):
        async with aiosqlite.connect(self.name) as db:
            result = await db.execute('SELECT num_warns FROM warns WHERE user_id = ? AND server_id = ?', (user_id, server_id))
            existing_warns = await result.fetchone()

            if existing_warns is None:
                await db.execute('INSERT INTO warns (user_id, server_id, num_warns) VALUES (?, ?, 1)', (user_id, server_id))
            else:
                new_warns = existing_warns[0] + 1
                await db.execute('UPDATE warns SET num_warns = ? WHERE user_id = ? AND server_id = ?', (new_warns, user_id, server_id))

            await db.commit()


    async def get_warns(self, user_id, server_id):
        async with aiosqlite.connect(self.name) as db:
            result = await db.execute('SELECT num_warns FROM warns WHERE user_id = ? AND server_id = ?', (user_id, server_id))
            warns = await result.fetchone()
            return warns[0] if warns else 0

