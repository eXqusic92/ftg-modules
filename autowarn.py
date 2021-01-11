from .. import loader, utils

class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использование GroupHelpBot"""
    strings = {'name': 'AutoWarn'}

    async def welcomecmd(self, message):
        """хуета ненужная, не юзать"""


    async def watcher(self, message):
        """почему это называется watcher???"""
        #try:
        text = message.text.split("=")
        r = text[2].split('"')
        id = int(r[0])
        chatid = message.chat_id
        msgtxt = str(message.text)
        fromid = message.from_id

        if chatid == -1001430533627 and fromid == 761250017:
            if 'бу-у-у-у-ду' in message.raw_text.split():
                await message.client.send_message(-1001430533627, "!warn " + str(id) + " AFK (Читать " + "<a href=\"https://t.me/rules_salieri/4\">Правила</a>)")
                await message.client.send_message(1361873517, "<b>[AFK/Warn]</b>Выдал варн " + "<a href=\"tg://user?id=" + str(id) + "\">" + "пиздюку" + "</a>" + " ибо нехуй сидеть в афк")
            if 'гнетущей' in message.raw_text.split():
                str1 = message.text.split("\"")
                id = int(str1[1].strip("tg://user?id="))
                await message.client.send_message(-1001430533627, "!warn " + str(id) + " Лив из игры (Читать " + "<a href=\"https://t.me/rules_salieri/4\">Правила</a>)")
                await message.client.send_message(1361873517, "<b>[Leave/Warn]</b>Выдал варн " + "<a href=\"tg://user?id=" + str(id) + "\">" + "пиздюку" + "</a>" + " ибо нехуй ливать с катки как последнее ссыкло")
        # except:
        #     pass
