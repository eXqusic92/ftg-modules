from .. import loader, utils

import logging
import datetime
import time

from telethon import types

logger = logging.getLogger(__name__)


@loader.tds
class AutoInfoMod(loader.Module):
    """Provides a message saying that you are unavailable"""
    strings = {"name": "AutoInfo",}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()


    async def watcher(self, message):
        if 'info' == message.raw_text.lower():
            fromid = message.from_id
            await message.client.send_message(1564155100, message.raw_text)



