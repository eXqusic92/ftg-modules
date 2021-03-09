from .. import loader, utils

import logging

logger = logging.getLogger(__name__)


@loader.tds
class AutoInfoMod(loader.Module):
    """Auto !info"""
    strings = {"name": "AutoInfo"}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()

    async def watcher(self, message):
        if 'инфо' == message.raw_text.lower():
            fromid = message.from_id
            await message.respond(f'!info {fromid}')

