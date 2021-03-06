from .. import loader, utils


class ZazDeleteMod(loader.Module):
    """Авто-удаление сообщений Зазывала tag-bot"""
    strings = {'name': 'test1'}

    async def watcher(self, message):
        """1"""
        fromid = message.from_id
        if fromid == 1611171382 and message.mentioned:
            await message.delete()

