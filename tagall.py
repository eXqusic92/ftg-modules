from .. import loader, utils
import time


def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'SalieriTag'}

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
