from .. import loader, utils

class MuteAllMod(loader.Module):
    """Автоподбор подарков из канала True Mafia"""
    strings = {'name': 'AutoGift'}

    async def watcher(self, event):
        """почему это называется watcher???"""
        if ('несколько' in event.raw_text.split()) or ('поделился' in event.raw_text.split()):
            result = await event.click()
            try:
                await event.client.send_message('me', result.message)
            except:
                pass
