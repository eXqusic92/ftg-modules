from .. import loader, utils

known_id = [508169464, 1564155100]
# known_id = [1564155100]

class ZazDeleteMod(loader.Module):
    """Авто-удаление сообщений Зазывала tag-bot"""
    strings = {'name': 'ZazDelete'}

    async def watcher(self, message):
        """Авто-удаление сообщений Зазывала tag-bot"""
        fromid = message.sender_id
        if message.raw_text.lower() == "бот!" and fromid in known_id:
            await message.reply("Приветствую, мой господин!🤝")
            return
        elif message.raw_text.lower() == "бот!" and fromid == 1404776819:
            await message.reply("Приветик, крошка ;)")
            return
        elif message.raw_text.lower() == "бот!" and fromid == 905964102:
            await message.reply("Приветик, соска Влада😘")
            return
        elif message.raw_text.lower() == "бот!" and fromid not in known_id:
            await message.reply("Ты че за ноунейм нах, съебни пока не дал пиздов тебе")
            return
