from .. import loader, utils

users = [725431547]

def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'Tt'}

    async def tagcmd(self, event):
        """Тэг-модуль пидоров для Bar of Don Salieri"""
        global users
        async for x in users:
            event.client.get_entity(x)
            event.reply(str(x.id))
