from .. import loader, utils


class AutoMessageMod(loader.Module):
    """берет все айди из чата .id {count}"""
    strings = {'name': 'id'}

    async def idcmd(self, message):
        """???"""
        args = utils.get_args(message)
        if args:
            count = int(args[0].strip())
        else:
            count = 200
            text = ""
            cnt = 0
        async for user in message.client.iter_participants(message.chat_id, limit=count, aggressive=True):
            text += str(user.id) + " " + str(user.first_name) + "\n"
            cnt += 1
            if cnt > 20:
                await message.client.send_message("me", text)
                cnt = 0
        await message.delete()
