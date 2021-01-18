from .. import loader, utils


def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'inv'}

    async def invitecmd(self, event):
        """Тэг-модуль пидоров для Bar of Don Salieri"""
        await event.delete()
        global text
        text = """
                Привет💕
                Отниму у тебя несколько минут твоего времени✨
                Хотела бы пригласить тебя в свой чат, где мы играем в Мафию🤠 там постоянный актив и стандартные правила.
                Если заинтересовало, скажи "да" и я скину тебе ссылку на чат❤️
                """
        args = utils.get_args(event)
        chat = await event.get_input_chat()

        if args:
            count = int(args[0].strip())
        else:
            count = 1

        async for x in event.client.iter_participants(chat, limit=count):
            await event.client.send_message(int(x.id), text)
