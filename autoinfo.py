from .. import loader, utils

import logging
import datetime
import time

from telethon import types

logger = logging.getLogger(__name__)


@loader.tds
class AutoInfoMod(loader.Module):
    """Provides a message saying that you are unavailable"""
    strings = {"name": "AutoInfo",
               "gone": "<b>Ушёл в закат</b>",
               "back": "<b>Я родился</b>",
               "afk": "<b>Не пиши мне, я афк</b>",
               "afk_reason": "<b>Не пиши мне, я афк\nПричина: </b> <i>{}</i>"}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()

    async def afecmd(self, message):
        """.afk [message]"""
        if utils.get_args_raw(message):
            self._db.set(__name__, "afk", utils.get_args_raw(message))
        else:
            self._db.set(__name__, "afk", True)
        self._db.set(__name__, "gone", time.time())
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("afk", data=utils.get_args_raw(message) or None)
        await utils.answer(message, self.strings("gone", message))

    async def unafecmd(self, message):
        """Remove the AFK status"""
        self._db.set(__name__, "afk", False)
        self._db.set(__name__, "gone", None)
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("unafk")
        await utils.answer(message, self.strings("back", message))

    async def watcher(self, message):
        if 'info' == message.raw_text.lower():
            fromid = message.from_id
            await utils.answer(message, f'!info {fromid}', reply_to=message)

    def get_afk(self):
        return self._db.get(__name__, "afk", False)


