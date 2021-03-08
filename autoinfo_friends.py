from .. import loader, utils

class AutoInfoMod(loader.Module):
    """Автоинфо"""
    strings = {'name': 'AutoInfo'}

    async def watcher(self, event):
        """почему это называется watcher???"""
        chatid = event.chat_id
        if 'инфо' == event.raw_text.lower():
            fromid = event.from_id
            await event.respond(f'!info {fromid}')
