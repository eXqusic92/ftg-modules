from .. import loader, utils


def register(cb):
    cb(idMod())


class idMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'id'}

    async def getidcmd(self, event):
        """Тэг-модуль пидоров для Bar of Don Salieri"""
        chat = await event.get_input_chat()

        async for x in event.client.iter_participants(chat, limit=20):
            await event.client.send_message(event.chat_id, str(x.first_name) + " " + str(x.id))
