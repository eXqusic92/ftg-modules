from .. import loader, utils
import asyncio


@loader.tds
class YourMod(loader.Module):
    """Msg Editor"""  # Translateable due to @loader.tds
    strings = {"name": "Message Editor",
               "after_sleep": "We have finished sleeping!"}

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def ilcmd(self, message):
        """.il [cnt] [word1] [word2]"""
        args = utils.get_args(message)
        try:
            count = int(args[0])
            word1 = args[1]
            word2 = args[2]
        except:
            await message.delete()
            return

        for x in range(count):
            await message.edit(word1)
            await asyncio.sleep(0.3)
            await message.edit(word2)
            await asyncio.sleep(0.3)
