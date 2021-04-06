from .. import loader, utils
import asyncio
import datetime

sud_state = False


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
        souch_ids = [1564155100, 504225012]
        vlad_id = 508169464
        if not sud_state:
            chatid = message.chat_id
            fromid = message.from_id

            if chatid == -1001430533627 and (fromid == 761250017 or fromid == 1044037207):
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
                                await message.client.send_message(1361873517, f"<a href=\"tg://user?id={str(uid)}\">{username}</a> сидит в афк псина\n\n{timestamp}")
                                await asyncio.sleep(0.2)
                                await message.respond("анрег")
                            elif uid in souch_ids:
                                await message.reply("!Уважаю")
                                await message.client.send_message(1361873517, f"Респект и уважение этому человеку <a href=\"tg://user?id={str(uid)}\">{username}</a>\n\n{timestamp}")
                                await asyncio.sleep(0.2)
                                await message.respond("анрег")
                            elif uid == vlad_id:
                                await message.reply("!Ладно")
                                await message.client.send_message(1361873517, f"Блять <a href=\"tg://user?id={str(uid)}\">Влад</a> ты пиздаball\n{timestamp}")
                                await asyncio.sleep(0.2)
                                await message.respond("анрег")
                            else:
                                await message.client.send_message(-1001430533627, f"!mute {str(uid)} 2 hours AFK (Читать <a href=\"https://t.me/rules_salieri/14\">Правила</a>). Последующая игра с мутом запрещена, наказание - варн!")
                                await message.client.send_message(1361873517, f"<b>[AFK/Mute] </b>Выдал мут <a href=\"tg://user?id={str(uid)}\">{username}</a> ибо нехуй сидеть в афк\n\n{timestamp}")
                                await asyncio.sleep(0.2)
                                await message.respond("анрег")
                                cnt = self._db.get("warns", "afk", 0)
                                self._db.set("warns", "afk", cnt+1)

                                afk_list = self._db.get("afk", "warns")
                                if username in afk_list:
                                    afk_list[username] = afk_list.get(username) + 1
                                    self._db.set("afk", "warns", afk_list)
                                else:
                                    afk_list = {**afk_list, username: 1}
                                    self._db.set("afk", "warns", afk_list)

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
                            await message.reply("!Ладно")
                            await message.client.send_message(1361873517, f"Krasav4ik - <a href=\"tg://user?id=\"{str(uid)}\">Влад</a>\n\n{timestamp}")
                            await asyncio.sleep(0.2)
                            await message.respond("анрег")
                        else:
                            await message.client.send_message(-1001430533627, f"!warn {str(uid)} Лив из игры (Читать <a href=\"https://t.me/rules_salieri/14\">Правила</a>)")
                            await message.client.send_message(1361873517, f"<b>[Leave/Warn] </b>Выдал варн <a href=\"tg://user?id={str(uid)}\">{username}</a> ибо нехуй ливать с катки как последнее ссыкло\n\n{timestamp}")
                            await asyncio.sleep(0.2)
                            await message.respond("анрег")
                            cnt = self._db.get("warns", "leave", 0)
                            self._db.set("warns", "leave", cnt + 1)

                            leave_list = self._db.get("leave", "warns")
                            if username in leave_list:
                                leave_list[username] = leave_list.get(username) + 1
                                self._db.set("leave", "warns", leave_list)
                            else:
                                leave_list = {**leave_list, username: 1}
                                self._db.set("leave", "warns", leave_list)