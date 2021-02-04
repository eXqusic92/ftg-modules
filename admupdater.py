from .. import loader, utils
import asyncio


@loader.tds
class admupdateMod(loader.Module):
    """Обновление списка админов Bar of Don Salieri"""
    strings = {"name": "AdmUpdate"}

    async def client_ready(self, client, db):
        self._db = db

    async def updcmd(self, event):
        """.upd"""
        await event.respond("<b>Обновляем список админов</b>")

        admins = []
        async for user in event.client.iter_participants(event.chat_id, limit=50):
            admins.append(user.id)
        admins.remove(508169464)
        admins.remove(1564155100)
        self._db.set(__name__, "admin_list", admins)
        await event.respond("<b>Список админов успешно обновлён!</b>")
