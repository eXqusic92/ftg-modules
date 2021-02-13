from .. import loader, utils

text = """
Привет, у тебя уже 6/6 варнов. Ты в бане. 
Нужно выполнять было задания, что бы снимать варны, они есть в наших правилах. 
Напиши <a href="tg://user?id=508169464">создателю</a>, что бы тебе подсказали, что надо сделать, что бы вернуться в чат.
Прочитай пожалуйста <a href="https://t.me/rules_salieri/14">Правила</a>)
Не отвечай на это сообщение, потому что я всего лишь бот. Напиши админам и они тебе помогут
        """

class AutoMessageMod(loader.Module):
    """Авто-уведомления пользователя о бане"""
    strings = {'name': 'AutoMessage'}

    async def watcher(self, message):
        """???"""
        fromid = message.from_id
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