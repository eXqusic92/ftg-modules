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
        admins.remove(1564155100)
        self._db.set("admins", "ids", admins)
        await event.respond("<b>Список админов успешно обновлён!</b>")

    async def admcmd(self, event):
        """Получить список действующих админов"""
        mentions = "<b>Список действующих админов:</b>\n"
        admin = self._db.get("admins", "ids", None)
        for aid in admin:
            usr = await event.client.get_entity(aid)
            mentions += f"►<a href=\"tg://user?id={usr.id}\">{usr.first_name}</a> - <code>{usr.id}</code>\n"
        await event.respond(mentions)
