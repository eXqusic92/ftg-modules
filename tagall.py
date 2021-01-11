from .. import loader, utils
from asyncio import sleep, gather


def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag Module for Bar of Don Salieri"""
    strings = {'name': 'Spam'}

    async def tagallcmd(self, message):
        """Обычный тэг-модуль"""
        mentions = ""
        counter = 0
        args = utils.get_args(message)
        chat = await message.get_input_chat()
        async for x in message.client.iter_participants(chat, args[0]):
            mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
            counter += 1
            if counter == 1:
                await message.reply(mentions)
                counter = 0
                mentions = ""
        if counter == 0:
            await message.delete()
            return
        await message.reply(mentions)
        await message.delete()
        #return await message.client.send_message(message.chat_id, '.tagall [количество юзеров(не больше 100)]')
