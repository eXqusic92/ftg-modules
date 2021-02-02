import telethon
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

# Use your own values from my.telegram.org
api_id = 2196711
api_hash = '5668721b41aa4a8fbaa0b2939bb7960c'
client = TelegramClient('anon', api_id, api_hash)


async def main():
    limit = 350

    salieri = await client.get_entity(-1001430533627)

    chat = await client.get_entity('https://t.me/CityWarsMafia')
    chat1 = await client.get_entity('https://t.me/TrueMafiaUA')
    chat2 = await client.get_entity('https://t.me/druzyachatt')
    chat3 = await client.get_entity('https://t.me/TrueMafia2')
    chat4 = await client.get_entity('https://t.me/Russkiy_Gruppa')
    chat5 = await client.get_entity('https://t.me/mafiaif')
    chat6 = await client.get_entity('https://t.me/werewolfru')
    chat7 = await client.get_entity('https://t.me/RDNO69')

    async for usr in client.iter_participants(chat7, limit=limit, aggressive=True):
        try:
            i = await client.get_entity(usr.id)
            if i.bot:
                print('bot')
                continue
            else:
                await client(InviteToChannelRequest(salieri, [i]))
                print('1')
        except Exception as e:
            print(e)
            continue
with client:
    client.loop.run_until_complete(main())

