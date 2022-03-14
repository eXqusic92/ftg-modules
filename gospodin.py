from .. import loader, utils


class ZazDeleteMod(loader.Module):
    """qq"""
    strings = {'name': 'Gospodin'}

    async def watcher(self, message):
        """qq"""
        fromid = message.sender_id
        if message.raw_text.lower() == "бот!":
            await message.reply("хуй!")
            return
