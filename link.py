from .. import loader, utils


class AutoMessageMod(loader.Module):
    """берет все айди из чата .id {count}"""
    strings = {'name': 'l'}

    async def lcmd(self, message):
        """???"""
        await message.respond(f"http://t.me/salieribar_bot?start={message.chat_id}\n\n С каждого твинка по этой ссылке перейди пж и нажми старт")
