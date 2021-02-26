from .. import loader, utils

known_id = [508169464, 1564155100]


class ZazDeleteMod(loader.Module):
    """Авто-удаление сообщений Зазывала tag-bot"""
    strings = {'name': 'ZazDelete'}

    async def watcher(self, message):
        """Авто-удаление сообщений Зазывала tag-bot"""
        fromid = message.from_id
        if message.raw_text.lower() == "бот!" and fromid in known_id:
            await message.reply("Приветствую, мой господин!🤝")
        elif message.raw_text.lower() == "бот!" and fromid not in known_id:
            await message.reply("Ты че за ноунейм нах, съебни пока не дал пиздов тебе")
