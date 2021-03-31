from .. import loader, utils
import telethon
from datetime import datetime, timedelta
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights


class AutoPinMod(loader.Module):
    """Автопин регистрации"""
    strings = {'name': 'AutoPin'}

    async def watcher(self, message):
        """почему это называется watcher???"""
        rights = ChatBannedRights(
            until_date=timedelta(seconds=1),
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True
        )
        for ent in message.entities:
            if type(ent) == telethon.types.MessageEntityUrl:
                channel = await message.client.get_entity(message.chat_id)
                user = await message.client.get_entity(message.from_id)
                s = message.raw_text[ent.offset:ent.offset+ent.length]
                if ('t.me/sng_casino' in s) or ('t.me/c/1348342488' in s) or ('sng_casino' in s):
                    return
                await message.client(EditBannedRequest(channel, user, rights))
                await message.delete()
                return
            if type(ent) == telethon.types.MessageEntityTextUrl:
                channel = await message.client.get_entity(message.chat_id)
                user = await message.client.get_entity(message.from_id)
                if ('t.me/sng_casino' in ent.url) or ('t.me/c/1348342488' in ent.url) or ('sng_casino' in ent.url):
                    return
                await message.client(EditBannedRequest(channel, user, rights))
                await message.delete()
                return
