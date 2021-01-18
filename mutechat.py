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
            await message.respond("<b>Эти жалкие людишки снова могут говорить!</b>")
        else:
            turned = True
            await message.respond("<b>Молчать всем!</b>")

    async def watcher(self, event):
        """почему это называется watcher???"""
        global turned, excl
        from_id = event.from_id
        msg1 = event.raw_text
        msg = msg1.lower()
        if msg == 'мут' and from_id in excl:
            if turned:
                turned = False
                await event.respond("<b>Эти жалкие людишки снова могут говорить!</b>")
            else:
                turned = True
                await event.respond("<b>Молчать всем!</b>")
        if turned:
            if from_id in excl:
                pass
            else:
                await event.delete()
