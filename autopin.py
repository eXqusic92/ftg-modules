from .. import loader, utils
import asyncio



class AutoPinMod(loader.Module):
    """Автопин регистрации"""
    strings = {'name': 'AutoPin'}

    async def watcher(self, message):
        """почему это называется watcher???"""
        baku_id = 1044037207
        chatid = [-1001430533627, -1001170767846]
        if (message.sender_id == baku_id) and (message.chat_id in chatid):
            if 'набор' in message.raw_text.split():
                await message.pin()
                await asyncio.sleep(5)
                await message.respond("/extend")
                return
            if ('ветров' in message.raw_text.split()) or ('Недостаточно' in message.raw_text.split()):
                x = await message.client.get_messages(message.chat_id, limit=30, from_user=baku_id)
                for msg in x:
                    if 'набор' in msg.raw_text.split():
                        await msg.delete()
