import datetime
from .. import loader, utils
from telethon.tl.types import ChannelParticipantsBanned

class AutoWarnforMuteMod(loader.Module):
    """AutoWarn for game with mute"""
    strings = {'name': 'MuteWarn'}

    async def watcher(self, message):
        """watcher"""
        time = datetime.datetime.now().time().replace(microsecond=0)
        date = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        timestamp = f'{time} | {date}.{month}.{year}'
        muted = []
        fromid = message.from_id
        chatid = message.chat_id
        msg = message.raw_text.split()
        if (chatid == -1001430533627) and (fromid == 1044037207):
            if 'длилась:' in msg:
                x = await message.client.get_participants(-1001430533627, limit=100, filter=ChannelParticipantsBanned)
                for i in x:
                    muted.append(i.id)
                for mid in muted:
                    await message.client.send_message("me", "muted - " + str(mid))
                for usr in message.entities:
                    if hasattr(usr, 'user_id'):
                        if usr.user_id in muted:
                            userent = await message.client.get_entity(usr.user_id)
                            if userent.last_name is None:
                                username = str(userent.first_name)
                            elif userent.last_name and userent.first_name:
                                username = str(userent.first_name) + " " + str(userent.last_name)
                            else:
                                username = str(userent.last_name)
                            await message.client.send_message(-1001430533627, f"!warn {str(usr.user_id)} Игра с мутом")
                            await message.client.send_message(1361873517, f"<b>[Игра с мутом/Warn] </b>Выдал варн <a href=\"tg://user?id={str(usr.user_id)}\">{username}</a> ибо этот пидорас играет с мутом\n\n{timestamp}")
