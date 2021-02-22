import telethon
from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import TypeChannelParticipantsFilter, ChannelParticipantsAdmins

api_id = 2196711
api_hash = '5668721b41aa4a8fbaa0b2939bb7960c'

client1 = TelegramClient('anon1', api_id, api_hash)
client2 = TelegramClient('anon2', api_id, api_hash)
client3 = TelegramClient('anon3', api_id, api_hash)
client4 = TelegramClient('anon4', api_id, api_hash)
client5 = TelegramClient('anon5', api_id, api_hash)
client6 = TelegramClient('anon6', api_id, api_hash)
client7 = TelegramClient('anon7', api_id, api_hash)
client8 = TelegramClient('anon8', api_id, api_hash)
client9 = TelegramClient('anon9', api_id, api_hash)
client10 = TelegramClient('anon10', api_id, api_hash)

counter = 0
accno = 0


async def main():
    # Проверка на спам
    global counter
    chat = '@SpamBot'
    async with client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True))
            await client.send_message(chat, '/start')
            response = await response
            if 'free' in response.raw_text.split():
                counter += 1
                print('Free accs -', counter, 'of 9')
            else:
                me = await client.get_me()
                name = me.first_name
                text1 = response.raw_text.split()
                dat = text1[text1.index('until') + 1:text1.index('until') + 5]
                date = " ".join(dat)
                print('Spam until', date, '-', name)
        except:
            pass

# async def main():
#     # Удаление всех диалогов
#     async for dialog in client.iter_dialogs():
#         await client.delete_dialog(dialog, revoke=True)
#     print("Done")

# async def main():
#     # Рассылка инвайт
#     global accno
#     chats = ['https://t.me/CityWarsMafia', 'https://t.me/TrueMafiaUA', 'https://t.me/druzyachatt', 'https://t.me/TrueMafia2',
#              'https://t.me/Russkiy_Gruppa', 'https://t.me/mafiaif', 'https://t.me/werewolfru', 'https://t.me/bakuclassesofficial',
#              'https://t.me/igorlinkmafia']
#     chat = await client.get_entity(chats[accno])
#     text = 'Привет) Давай с нами играть в мафию? У нас очень веселая компания, честно)'
#     limit = 40
#
#     admins = []
#
#     async for usr in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
#         admins.append(usr.id)
#
#     async for usr in client.iter_participants(chat, limit=limit):
#         try:
#             i = await client.get_entity(usr.id)
#             if i.id in admins:
#                 print('admin')
#                 continue
#             if i.bot:
#                 print('bot')
#                 continue
#             else:
#                 await client.send_message(usr, text)
#                 print('1')
#         except Exception as e:
#             print(e)
#             continue
#     accno += 1


# async def main():  # инвайт
#     global accno
#     chats = ['https://t.me/CityWarsMafia',
#              'https://t.me/TrueMafiaUA',
#              'https://t.me/werewolfru',
#              'https://t.me/druzyachatt',
#              'https://t.me/bakuclassesofficial',
#              'https://t.me/TrueMafia2',
#              'https://t.me/Russkiy_Gruppa',
#              'https://t.me/mafiaif',
#              'https://t.me/igorlinkmafia']
#     chat = await client.get_entity(chats[accno])
#     friends = await client.get_entity(-1001170767846)
#     text = 'Привет) Давай с нами играть в мафию? У нас очень веселая компания, честно)'
#     limit = 60
#
#     admins = []
#     users_to_invite = []
#
#     async for usr in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
#         admins.append(usr.id)
#
#     async for usr in client.iter_participants(chat, limit=limit, aggressive=True):
#         try:
#             i = await client.get_entity(usr.id)
#             if i.id in admins:
#                 print('admin')
#                 continue
#             if i.bot:
#                 print('bot')
#                 continue
#             else:
#                 users_to_invite.append(usr)
#                 if len(users_to_invite) > 20:
#                     await client(InviteToChannelRequest(friends, users_to_invite))
#                     print('1 -', accno)
#                     users_to_invite = []
#         except Exception as e:
#             print(e)
#             continue
#     await client(InviteToChannelRequest(friends, users_to_invite))
#     accno += 1


with client1 as client:
    client.loop.run_until_complete(main())

with client2 as client:
    client.loop.run_until_complete(main())

with client3 as client:
    client.loop.run_until_complete(main())

with client4 as client:
    client.loop.run_until_complete(main())

with client5 as client:
    client.loop.run_until_complete(main())

with client6 as client:
    client.loop.run_until_complete(main())

with client7 as client:
    client.loop.run_until_complete(main())

with client8 as client:
    client.loop.run_until_complete(main())

with client9 as client:
    client.loop.run_until_complete(main())

with client10 as client:
    client.loop.run_until_complete(main())
