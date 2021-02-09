from .. import loader, utils
import asyncio


def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'SalieriTag'}

    async def client_ready(self, client, db):
        self._db = db

    async def updcmd(self, event):
        """.upd"""
        await event.respond("<b>Обновляем список админов</b>")

        admins = []
        async for user in event.client.iter_participants(event.chat_id, limit=50):
            admins.append(user.id)
        self._db.set("admins", "ids", admins)
        await event.respond("<b>Список админов успешно обновлён!</b>")

    async def watcher(self, event):
        """Тэг-модуль пидоров для Bar of Don Salieri"""
        global text, count
        mssg = event.raw_text.split()
        mssg = [x.lower() for x in mssg]
        admin_ids = self._db.get("admins", "ids", None)
        fromid = event.from_id
        chatid = event.chat_id
        if (('калл' in mssg) or ('каллалл' in mssg) or ('каллал' in mssg) or ('каллактив' in mssg)) and (fromid in admin_ids):
            try:
                unreg = [1564155100, 595975466]
                mentions = ""
                counter = 0
                chat = await event.get_input_chat()

                if len(mssg) == 1:
                    count = 100
                    text = None
                elif len(mssg) == 2:
                    try:
                        count = int(mssg[1])
                        text = None
                    except:
                        count = 100
                        text = str(mssg[1])
                elif len(mssg) > 2:
                    try:
                        count = int(mssg[1])
                        text = " ".join(mssg[1:])
                    except:
                        count = 100
                        text = " ".join(mssg[1:])
                start = await event.client.send_message(chatid, "<b>!Призыв участников начат</b>")
                async for x in event.client.iter_participants(chat, limit=count, aggressive=True):
                    if x.id in unreg:
                        continue
                    if text:
                        mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + text + "</a>"
                    else:
                        mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + x.first_name + "</a>"
                    counter += 1
                    if counter == 1:
                        msg = await event.client.send_message(chatid, mentions, reply_to=start)
                        if not msg.is_reply:
                            await event.respond("<b>!Призыв остановлен</b>")
                            return
                        await msg.delete()
                        counter = 0
                        mentions = ""
                if counter == 0:
                    await event.delete()
                    await asyncio.sleep(0.2)
                    await event.client.send_message(chatid, "анрег")
                    return
                await event.reply(mentions)
                await event.delete()
            except Exception as e:
                await event.client.send_message(event.chat_id, f'!Ты еблан блять? Введи .tagall [количество юзеров(не больше 100), по дефолту 20]\n\n{e}')
                await asyncio.sleep(0.2)
                await event.client.send_message(chatid, "анрег")
