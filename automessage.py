from .. import loader, utils

text = """
Привет. Тебя забанили за максимальное количество варнов. Есть  3 выхода: 
1. В @salieribar_bot купить разбан и написать админам за ссылку обратно
2. Ждать 4 дня и написать админам, что бы те дали ссылку
3. Так же ждать, но поиграть во 2 нашем чате, литтл баре
Выбирай вариант и пиши @DANDYMOROZOW"""

class AutoMessageMod(loader.Module):
    """Авто-уведомления пользователя о бане"""
    strings = {'name': 'AutoMessage'}

    async def watcher(self, message):
        """???"""
        fromid = message.sender_id
        chatid = message.chat_id
        if chatid == -1001430533627 and fromid == 1237190930:
            if "(6 из 6)" and "заблокировал" in message.raw_text:
                userid = message.entities[0].user_id
                await message.client.send_message(userid, text)
                userent = await message.client.get_entity(userid)
                if userent.last_name is None:
                    username = str(userent.first_name)
                elif userent.last_name and userent.first_name:
                    username = str(userent.first_name) + " " + str(userent.last_name)
                else:
                    username = str(userent.last_name)
                await message.client.send_message(1361873517, f'🚫Забанил <a href="tg://user?id={userid}">{username}</a> за получение 6 варна')
