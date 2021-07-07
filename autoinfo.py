from .. import loader, utils

import logging
import datetime
import time

from telethon import types

logger = logging.getLogger(__name__)


@loader.tds
class AutoInfoMod(loader.Module):
    """1"""
    strings = {"name": "AutoInfo"}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()


    async def watcher(self, message):
        if 'инфо' == message.raw_text.lower():
            reply = await message.get_reply_message()
            fromid = message.from_id
            if reply:
                await message.respond(f"!info {reply.sender_id}")
                return
            await message.respond(f"!info {message.sender_id}")



