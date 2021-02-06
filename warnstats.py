from .. import loader, utils


class WarnStatsMod(loader.Module):
    """Статистика варнов"""
    strings = {'name': 'WarnStats'}

    async def client_ready(self, client, db):
        self._db = db

    async def statscmd(self, event):
        """.stats"""
        afks = self._db.get("warns", "afk", 0)
        leaves = self._db.get("warns", "leave", 0)

        text = f"""
<b>За сегодня было выдано варнов:</b>

<i>За АФК - {afks}
За лив - {leaves}</i>

Статистика сброшена
"""
        event.respond(text)
        self._db.set("warns", "afk", 0)
        self._db.set("warns", "leave", 0)
