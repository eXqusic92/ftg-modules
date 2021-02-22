import telethon
from telethon import TelegramClient
from telethon import events
api_id = 2196711
api_hash = '5668721b41aa4a8fbaa0b2939bb7960c'

client = TelegramClient('anon10', api_id, api_hash)


async def main():
    me = await client.get_me()
    print(me)
with client as client:
    client.loop.run_until_complete(main())