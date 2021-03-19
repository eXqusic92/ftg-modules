from .. import loader, utils


class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'helper'}

    async def client_ready(self, client, db):
        self._db = db

    async def watcher(self, message):
        """почему это называется watcher???"""
        func = message.raw_text.split(':')
        if message.from_id != 1657808514:
            return
        if message.raw_text.split(':')[0] != "action":
            return
        await message.client.send_message(-1001430533627, f"!{func[1]} {func[2]}")