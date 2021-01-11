from .. import loader, utils


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
                if text:
                    mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + text + "</a>"
                else:
                    mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + x.first_name + "</a>"
                counter += 1
                if counter == 1:
                    await event.client.send_message(event.chat_id, mentions)
                    counter = 0
                    mentions = ""
            if counter == 0:
                await event.delete()
                return
            await event.reply(mentions)
            await event.delete()
        except:
            return await event.client.send_message(event.chat_id, 'Ты еблан блять? Введи .tagall [количество юзеров(не больше 100), по дефолту 20]')
