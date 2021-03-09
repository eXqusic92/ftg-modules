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

    async def switchcmd(self, message):
        await message.respond("on")
    
    async def watcher(self, message):
        if 'info' == message.raw_text.lower():
            fromid = message.from_id
            await utils.answer(message, f'!info {fromid}', reply_to=message)
