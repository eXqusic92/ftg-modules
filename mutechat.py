from .. import loader, utils

turned = False
excl = [508169464, 1564155100]

class MuteAllMod(loader.Module):
    """АвтоДжоин для бота Мафии"""
    strings = {'name': 'MuteChat'}

    async def amutecmd(self, message):
        """Включить/выключить удаление всех сообщений в чате"""
        global turned
        if turned:
            turned = False
            await message.edit("<b>Эти жалкие людишки снова могут говоритЬ!</b>")
        else:
            turned = True
            await message.edit("<b>Молчать всем!</b>")

    async def watcher(self, message):
        """почему это называется watcher???"""
        global turned, excl
        if turned:
            from_id = message.from_id
            if from_id in excl and message.chat_id == -1001430533627:
                pass
            else:
                message.delete()
