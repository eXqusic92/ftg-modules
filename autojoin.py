from .. import loader, utils

turned = False

class AutoJoinMod(loader.Module):
    """АвтоДжоин для бота Мафии"""
    strings = {'name': 'AutoJoin'}

    async def ajoincmd(self, message):
        """Включить/выключить функцию автоконнекта к игре"""
        global turned
        if turned:
            turned = False
            await message.edit("<b>Функция авто-джоина выключена</b>")
        else:
            turned = True
            await message.edit("<b>Функция авто-джоина включена</b>")

    async def watcher(self, message):
        """почему это называется watcher???"""
        global turned
        if turned:
            from_id = message.from_id
            text = 'Начинается'
            msgtext = message.text.split()
            if from_id == 761250017 and text in msgtext:
                await message.click(0)