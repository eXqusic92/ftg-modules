from .. import loader, utils
import asyncio
import datetime

sud_state = False


class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'AutoWarn_FriendsMafia'}

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

        pass_roles = ["Мирный", "Счастливчик", "Санта", "Маньяк", "Самоубийца"]
        pass_roles_1 = ["житель", "Счастливчик", "Санта", "Маньяк", "Самоубийца"]
        admin_ids = self._db.get("admins", "ids", None)
        if not sud_state:
            chatid = message.chat_id
            fromid = message.from_id

            if chatid == -1001170767846 and fromid == 761250017:
                if ('убит' in message.raw_text.split()) and ("гостях" not in message.raw_text.split()):
                    if message.raw_text.split()[5] in pass_roles:
                        return
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
                                await message.client.send_message(-1001177665247, f"Админ <a href=\"tg://user?id={str(uid)}\">{username}</a> сидит в афк\n\n{timestamp}")
                            else:
                                await message.client.send_message(-1001170767846, f"!warn {str(uid)} AFK")
                                await message.client.send_message(-1001177665247, f"<b>[AFK/Mute] </b>Выдал варн <a href=\"tg://user?id={str(uid)}\">{username}</a> за афк\n\n{timestamp}")
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
                    x = await message.client.get_messages(-1001170767846, 15)
                    for msg in x:
                        msgs.append(msg.raw_text)

                    if msgs.count(message.raw_text) > 1:
                        pass
                    else:
                        if message.raw_text.split()[::-1][0] in pass_roles_1:
                            return
                        uid = message.entities[0].user_id
                        userent = await message.client.get_entity(uid)
                        if userent.last_name is None:
                            username = str(userent.first_name)
                        elif userent.last_name and userent.first_name:
                            username = str(userent.first_name) + " " + str(userent.last_name)
                        else:
                            username = str(userent.last_name)
                        if uid in admin_ids:
                            await message.client.send_message(-1001177665247, f"Админ <a href=\"tg://user?id={str(uid)}\">{username}</a> ливнул из катки\n\n{timestamp}")
                        else:
                            await message.client.send_message(-1001170767846, f"!warn {str(uid)} Лив из игры")
                            await message.client.send_message(-1001177665247, f"<b>[Leave/Warn] </b>Выдал варн <a href=\"tg://user?id={str(uid)}\">{username}</a> за лив\n\n{timestamp}")

                            cnt = self._db.get("warns", "leave", 0)
                            self._db.set("warns", "leave", cnt + 1)

                            leave_list = self._db.get("leave", "warns")
                            if username in leave_list:
                                leave_list[username] = leave_list.get(username) + 1
                                self._db.set("leave", "warns", leave_list)
                            else:
                                leave_list = {**leave_list, username: 1}
                                self._db.set("leave", "warns", leave_list)
