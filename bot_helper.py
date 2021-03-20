from .. import loader, utils


class BotHelperMod(loader.Module):
    """хелпер бота"""
    strings = {'name': 'helper'}

    async def watcher(self, message):
        """почему это называется watcher???"""
        func = message.raw_text.split(':')
        if message.from_id != 1657808514:
            return
        if message.raw_text.split(':')[0] != "action":
            return
        await message.client.send_message(-1001430533627, f"!{func[1]} {func[2]}")
        return
