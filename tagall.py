import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantsBots
from uniborg.util import admin_cmd
from .. import utils


@borg.on(admin_cmd("tagall"))
async def _(event):
    if event.fwd_from:
        return
    mentions = ""
    counter = 0
    args = utils.get_args(message)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, args[0]):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
        counter += 1
        if counter == 1:
            await event.reply(mentions)
            counter = 0
            mentions = ""
    if counter == 0:
        await event.delete()
        return
    await event.reply(mentions)
    await event.delete()
