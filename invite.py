import telethon
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import TypeChannelParticipantsFilter, ChannelParticipantsAdmins

api_id = 2196711
api_hash = '5668721b41aa4a8fbaa0b2939bb7960c'
client = TelegramClient('anon', api_id, api_hash)


async def main():
    text = 'Привет) Давай с нами играть в мафию? У нас очень веселая компания, честно)'
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
    chat8 = await client.get_entity('https://t.me/mafia111111111234689')

    admins = []

    async for usr in client.iter_participants(chat8, filter=ChannelParticipantsAdmins):
        admins.append(usr.id)

    async for usr in client.iter_participants(chat8, limit=limit, aggressive=True):
        try:
            i = await client.get_entity(usr.id)
            if i.id in admins:
                print('admin')
                continue
            if i.bot:
                print('bot')
                continue
            else:
                await client.send_message(usr, text)
                print('1')
        except Exception as e:
            print(e)
            continue
with client:
    client.loop.run_until_complete(main())

