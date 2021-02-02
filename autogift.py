from .. import loader, utils

class MuteAllMod(loader.Module):
    """Автоподбор подарков из канала True Mafia"""
    strings = {'name': 'AutoGift'}

    async def watcher(self, event):
        """почему это называется watcher???"""
        if 'подарков' in event.raw_text.split():
            await event.click()