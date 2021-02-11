from .. import loader, utils


class AutoPinMod(loader.Module):
    """Автопин регистрации"""
    strings = {'name': 'AutoPin'}

    async def watcher(self, message):
        """почему это называется watcher???"""
        baku_id = 1044037207
        chatid = -1001430533627
        if (message.from_id == baku_id) and (message.chat_id == chatid):
            if 'набор' in message.raw_text.split():
                await message.pin()
                return
            if ('ветров' in message.raw_text.split()) or ('Недостаточно' in message.raw_text.split()):
                x = await message.client.get_messages(-1001430533627, limit=30, from_user=baku_id)
                for msg in x:
                    if 'набор' in msg.raw_text.split():
                        await msg.delete()
