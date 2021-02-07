from .. import loader, utils


class WarnStatsMod(loader.Module):
    """Статистика варнов"""
    strings = {'name': 'WarnStats'}

    async def client_ready(self, client, db):
        self._db = db

    async def statscmd(self, event):
        """.stats"""
        afk_count = self._db.get("warns", "afk", 0)
        leave_count = self._db.get("warns", "leave", 0)

        text = "<b>За сегодня было выдано варнов:\n\n</b><i>За АФК:\n</i>"
        afk_list = self._db.get("afk", "warns")
        leave_list = self._db.get("leave", "warns")
        a = sorted(afk_list.items(), key=lambda x: x[1], reverse=True)
        b = sorted(leave_list.items(), key=lambda x: x[1], reverse=True)

        afk_list_sorted = dict(a)
        leave_list_sorted = dict(b)
        if len(afk_list_sorted) == 0:
            text += "Нету варнов\n\n"
        else:
            for i in afk_list_sorted:
                text += f"{i} - {afk_list_sorted.get(i)}\n"
            text += f"<u>Всего за сегодня - {afk_count}</u>\n\n"

        text += "<i>За лив:\n</i>"
        if len(leave_list_sorted) == 0:
            text += "Нету варнов\n\n"
        else:
            for i in leave_list_sorted:
                text += f"{i} - {leave_list_sorted.get(i)}\n"
            text += f"<u>Всего за сегодня - {leave_count}</u>"
        await event.edit(text)
        self._db.set("afk", "warns", {})
        self._db.set("leave", "warns", {})
        self._db.set("warns", "afk", 0)
        self._db.set("warns", "leave", 0)
