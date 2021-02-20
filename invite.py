import telethon
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import TypeChannelParticipantsFilter, ChannelParticipantsAdmins

api_id = 3136893
api_hash = 'd5ac3a22ce29f8317733f4b4100e23c3'
client = TelegramClient('anon', api_id, api_hash)


async def main():


    # salieri = await client.get_entity(-1001430533627)
    # chat = await client.get_entity('https://t.me/CityWarsMafia')
    # chat = await client.get_entity('https://t.me/TrueMafiaUA')
    # chat = await client.get_entity('https://t.me/druzyachatt')
    # chat = await client.get_entity('https://t.me/TrueMafia2')
    # chat = await client.get_entity('https://t.me/Russkiy_Gruppa')
    # chat = await client.get_entity('https://t.me/mafiaif')
    # chat = await client.get_entity('https://t.me/werewolfru')
    # chat = await client.get_entity('https://t.me/RDNO69')
    # chat = await client.get_entity('https://t.me/TrueMafiaChat')
    # chat = await client.get_entity('https://t.me/MafiaCitySky')
    # chat = await client.get_entity('https://t.me/bakuclassesofficial')
    chat = await client.get_entity('https://t.me/MafiaCityClassic')

    admins = []
    text = 'Привет) Давай с нами играть в мафию? У нас очень веселая компания, честно)'
    limit = 70

    async for usr in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        admins.append(usr.id)

    async for usr in client.iter_participants(chat, limit=limit, aggressive=True):
        try:
            i = await client.get_entity(usr.id)
            if i.id in admins:
                print('admin')
                continue
            if i.bot:
                print('bot')
                continue
            else:
                await client.send_message(i.id, text)
                print('1')
                await asyncio.sleep(0.5)
        except Exception as e:
            print(e)
            continue

with client:
    client.loop.run_until_complete(main())

