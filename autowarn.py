# .eval text = reply.text.split("=")
# r = text[2].split('"')
# id = int(r[0])
# return id

import asyncio
from telethon import events, client

@client.on(events.NewMessage(pattern='(?i)hello.+'))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    await event.reply('Hey!')