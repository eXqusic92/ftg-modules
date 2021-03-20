from .. import loader, utils

zaz_id = [1263064901, 1169085389, 992657608, 803468136, 1362911415, 1302580284, 1355938374, 1383076852, 1283484635, 1181613391]


class ZazDeleteMod(loader.Module):
    """Авто-удаление сообщений Зазывала tag-bot"""
    strings = {'name': 'ZazDelete'}

    async def watcher(self, message):
        """Авто-удаление сообщений Зазывала tag-bot"""
        fromid = message.from_id
        msg = message.raw_text.split()
        if fromid in zaz_id:
            if 'неактивности' not in msg:
                if 'призывает' not in msg:
                    if 'снова' not in msg:
                        if len(msg) >= 2:
                            await message.delete()