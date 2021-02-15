from .. import loader, utils
from telethon.tl.types import ChannelParticipantsBanned

class AutoWarnforMuteMod(loader.Module):
    """AutoWarn for game with mute"""
    strings = {'name': 'MuteWarn'}

    async def watcher(self, message):
        """watcher"""
        muted = []
        fromid = message.from_id
        chatid = message.chat_id
        msg = message.raw_text.split()
        if (chatid == -1001430533627) and (fromid == 1044037207):
            if 'длилась:' in msg:
                x = await client.get_participants(-1001430533627, limit=100, filter=ChannelParticipantsBanned)
                for i in x:
                    muted.append(i.id)
                for usr in message.entities:
                    if hasattr(usr, 'user_id'):
                        if usr.user_id in muted:
                            await message.client.send_message(-1001430533627, f"!warn {usr.user_id} Игра с мутом")
