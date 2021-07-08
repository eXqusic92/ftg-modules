from .. import loader, utils
import asyncio
import datetime
from random import choice

sud_state = False

bar_messages = [
    "Бля, ну это случилось в баре, там вроде ровные штрихи играют, но этот пидорас.",
    "Чат - бар. Забаньте уже этого пидора.",
    "Ладно, бар норм чат вроде как, ругаться не буду",
    "Гондон ты блять. Не заслуживаешь играть в баре."
]

little_bar_messages = [
    "Ну чел с литла то, там одни додики играют, неудивительно.",
    "Ебаный литл...",
    "Сука блять. Кто там в литле главные? Крис? Леся? Вы блять кого там воспитали? Одни придурки играют",
    "Литл - чат додиков которые только и могут ливать и афкшить"
]


class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'AutoWarn'}

    async def client_ready(self, client, db):
        self._db = db

    async def turncmd(self, event):
        """Вкл/выкл автоварн"""
        global sud_state
        if sud_state:
            sud_state = False
            await event.respond("<b>Автоварн включен</b>")
            await asyncio.sleep(0.2)
            await event.respond("анрег")
        else:
            sud_state = True
            await event.respond("<b>Автоварн выключен</b>")
            await asyncio.sleep(0.2)
            await event.respond("анрег")

    async def watcher(self, message):
        """почему это называется watcher???"""
        global sud_state

        time = datetime.datetime.now().time().replace(microsecond=0)
        date = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        timestamp = f'{time} | {date}.{month}.{year}'

        admin_ids = self._db.get("admins", "ids", None)
        souch_ids = [1564155100]
        vlad_id = 508169464
        if not sud_state:
            chatid = message.chat_id
            fromid = message.sender_id

            if ((chatid == -1001430533627) or (chatid == -1001170767846)) and (fromid == 761250017 or fromid == 1044037207):
                if ('бу-у-у-у-ду' in message.raw_text.split()) or ('пообещал' in message.raw_text.split()):
                    for usr in message.entities:
                        if hasattr(usr, 'user_id'):
                            uid = usr.user_id
                            userent = await message.client.get_entity(uid)
                            if userent.last_name is None:
                                username = str(userent.first_name)
                            elif userent.last_name and userent.first_name:
                                username = str(userent.first_name) + " " + str(userent.last_name)
                            else:
                                username = str(userent.last_name)

                            if uid in admin_ids:
                                await message.reply("!Вот петушара, админ, ещё и АФКшит...")
                                await message.client.send_message(1361873517, f"<a href=\"tg://user?id={str(uid)}\">{username}</a> сидит в афк псина")
                            elif uid in souch_ids:
                                await message.reply("!Уважаю")
                                await message.client.send_message(1361873517, f"Респект и уважение этому человеку <a href=\"tg://user?id={str(uid)}\">{username}</a>\n\n{timestamp}")
                            elif uid == vlad_id:
                                await message.reply("!Снова со своей ламбой играецца, вот и забыл об игре")
                                await message.client.send_message(1361873517, f"Блять <a href=\"tg://user?id={str(uid)}\">Влад</a> ты пиздаball\n{timestamp}")
                            else:
                                await message.respond(f"!mute {str(uid)} 2 hours AFK (Читать <a href=\"https://t.me/rules_salieri/14\">Правила</a>). Последующая игра с мутом запрещена, наказание - варн!")
                                text = f"<b>[АФК сука]</b> Заткнул рот хуем на два (two) часа этому челу - <a href=\"tg://user?id={str(uid)}\">{username}</a> потому что еблана мамка кушать позвала. "
                                if chatid == -1001430533627:
                                    text += choice(bar_messages)
                                elif chatid == -1001170767846:
                                    text += choice(little_bar_messages)
                                await message.client.send_message(1361873517, text)
                                # cnt = self._db.get("warns", "afk", 0)
                                # self._db.set("warns", "afk", cnt+1)
                                #
                                # afk_list = self._db.get("afk", "warns")
                                # if username in afk_list:
                                #     afk_list[username] = afk_list.get(username) + 1
                                #     self._db.set("afk", "warns", afk_list)
                                # else:
                                #     afk_list = {**afk_list, username: 1}
                                #     self._db.set("afk", "warns", afk_list)

                if 'гнетущей' in message.raw_text.split():
                    msgs = []
                    x = await message.client.get_messages(-1001430533627, 15)
                    for msg in x:
                        msgs.append(msg.raw_text)

                    if msgs.count(message.raw_text) > 1:
                        return
                    else:
                        uid = message.entities[0].user_id
                        userent = await message.client.get_entity(uid)
                        if userent.last_name is None:
                            username = str(userent.first_name)
                        elif userent.last_name and userent.first_name:
                            username = str(userent.first_name) + " " + str(userent.last_name)
                        else:
                            username = str(userent.last_name)
                        if uid in admin_ids:
                            await message.reply("!Нахуй ливаешь, долбоёб?")
                            await message.client.send_message(1361873517, f"Ало <a href=\"tg://user?id={str(uid)}\">{username}</a> ты зашёл в катку чтобы повыпендриваться? Так сиди до конца, а не ливай посреди катки как крыса.\n\n{timestamp}")
                            await asyncio.sleep(0.2)
                            await message.respond("анрег")
                        elif uid in souch_ids:
                            await message.reply("!Ну и пошёл нахуй отсюдава")
                            await message.client.send_message(1361873517, f"<a href=\"tg://user?id={str(uid)}\">{username}</a> съебался с катки преждевременно.\n\n{timestamp}")
                            await asyncio.sleep(0.2)
                            await message.respond("анрег")
                        elif uid == vlad_id:
                            await message.reply("! Влад зассал потому что против него играют слишком сильные соперники")
                            await message.client.send_message(1361873517, f"Влад зассал потому что против него играют слишком сильные соперники")
                            await asyncio.sleep(0.2)
                            await message.respond("анрег")
                        else:
                            await message.respond(f"!warn {str(uid)} Лив из игры (Читать <a href=\"https://t.me/rules_salieri/14\">Правила</a>)")
                            text = f"<b>[Лив нахуй]</b> Хуеглот ебучий отхватил варн (вот этот если чо <a href=\"tg://user?id={str(uid)}\">{username}</a>) потому что он поступил как быдло и съебался с катки. "
                            if chatid == -1001430533627:
                                text += choice(bar_messages)
                            elif chatid == -1001170767846:
                                text += choice(little_bar_messages)
                            await message.client.send_message(1361873517, text)
                            # cnt = self._db.get("warns", "leave", 0)
                            # self._db.set("warns", "leave", cnt + 1)
                            #
                            # leave_list = self._db.get("leave", "warns")
                            # if username in leave_list:
                            #     leave_list[username] = leave_list.get(username) + 1
                            #     self._db.set("leave", "warns", leave_list)
                            # else:
                            #     leave_list = {**leave_list, username: 1}
                            #     self._db.set("leave", "warns", leave_list)
