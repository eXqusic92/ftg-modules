import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class YourMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"name": "AutoInfo"}

    async def watcher(self, event):
        """почему это называется watcher???"""
        chatid = event.chat_id
        if 'инфо' == event.raw_text.lower() and chatid == -1001430533627:
            fromid = event.from_id
            await event.respond(f'!info {fromid}')
