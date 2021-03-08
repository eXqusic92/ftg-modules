from .. import loader, utils


class ZazDeleteMod(loader.Module):
    """test"""
    strings = {'name': 'влал!'}

    async def client_ready(self, client, db):
        self._db = db

    async def watcher(self, message):
        """1"""
        if message.raw_text.lower() == 'влал!':
            await utils.answer(message, await self._db.fetch_asset(3))
