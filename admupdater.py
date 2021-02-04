from .. import loader, utils
import asyncio


@loader.tds
class admupdateMod(loader.Module):
    """Provides a message saying that you are unavailable"""
    strings = {"name": "AdmUpdate"}

    async def client_ready(self, client, db):
        self._db = db

    async def updcmd(self, message):
        """.afk [message]"""
        await message.edit("<b>Обновляем список админов</b>")
        await asyncio.sleep(0.6)
        await message.edit("<b>Обновляем список админов.</b>")
        await asyncio.sleep(0.6)
        await message.edit("<b>Обновляем список админов..</b>")
        await asyncio.sleep(0.6)
        await message.edit("<b>Обновляем список админов...</b>")

        admins = []
        async for user in message.client.iter_participants(message.chat_id, limit=50):
            admins.append(user.id)
        admins.remove(508169464)
        admins.remove(1564155100)
        self._db.set(__name__, "admin_list", admins)
        await message.edit("<b>Список админов успешно обновлён!</b>")
