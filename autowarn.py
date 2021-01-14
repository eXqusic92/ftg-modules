from .. import loader, utils

class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использование GroupHelpBot"""
    strings = {'name': 'AutoWarn'}

    async def welcomecmd(self, message):
        """хуета ненужная, не юзать"""


    async def watcher(self, message):
        """почему это называется watcher???"""

        admin_ids = [1028692153, 725431547, 895755815, 540902565, 883140642, 986002157, 1482857182, 754756140, 491255683, 1001187772]
        souch_ids = [1564155100, 504225012]
        vlad_id = 508169464
        #try:
        text = message.text.split("=")
        r = text[2].split('"')
        id = int(r[0])
        chatid = message.chat_id
        msgtxt = str(message.text)
        fromid = message.from_id

        if chatid == -1001430533627 and fromid == 761250017:
            if 'бу-у-у-у-ду' in message.raw_text.split():
                if id in admin_ids:
                    await message.reply("!Вот петушара, админ, ещё и АФКшит...")
                    await message.client.send_message(1361873517, "Слыш ты бля " + "<a href=\"tg://user?id=" + str(id) + "\">" + "чурка ебаная" + "</a>" + " хули ты в афк сидишь. Ты админ, лицо чата - тебе это непозволительно. Пиздец нынче админы пошли...")
                elif id in souch_ids:
                    await message.reply("!ЛЮДИ, СМОТРИТЕ!!! ЭТО СОУЧРЕДИТЕЛЬ ЧАТА НАЗЫВАЕТСЯ АХАХАХХАХ")
                    await message.client.send_message(1361873517, "Ебать " + "<a href=\"tg://user?id=" + str(id) + "\">" + "братишка" + "</a>" + " ты вкрай охуел быть соучем в группе и в афк сидеть")
                elif id == vlad_id:
                    await message.reply("!Влад, ну бля, ну как так... Хотя ладно, Владу простительно ибо если бы не он - вас бы тут не было. Но он все равно пидор")
                    await message.client.send_message(1361873517, "Блять" + "<a href=\"tg://user?id=" + str(id) + "\">" + "Влад" + "</a>" + " хули ты сам сидишь и дрочеш в группе, а на других орёшь что они афк? А?А?А?А?")
                else:
                    await message.client.send_message(-1001430533627, "!warn " + str(id) + " AFK (Читать " + "<a href=\"https://t.me/rules_salieri/4\">Правила</a>)")
                    await message.client.send_message(1361873517, "<b>[AFK/Warn] </b>Выдал варн " + "<a href=\"tg://user?id=" + str(id) + "\">" + "пиздюку" + "</a>" + " ибо нехуй сидеть в афк")

            if 'гнетущей' in message.raw_text.split():
                str1 = message.text.split("\"")
                id = int(str1[1].strip("tg://user?id="))
                if id in admin_ids:
                    await message.reply("!Админ - ссыкло!!!. На доску позора его!")
                    await message.client.send_message(1361873517, "Ало " + "<a href=\"tg://user?id=" + str(id) + "\">" + "блядь" + "</a>" + " ты зашёл в катку чтобы повыпендриваться? Так сиди до конца, а не ливай посреди катки как крыса.")
                elif id in souch_ids:
                    await message.reply("!ЛЮДИ, СМОТРИТЕ!!! ЭТО СОУЧРЕДИТЕЛЬ ЧАТА НАЗЫВАЕТСЯ АХАХАХХАХ")
                    await message.client.send_message(1361873517, "Ммм.. Хорошая попытка сбежать, мой " + "<a href=\"tg://user?id=" + str(id) + "\">" + "друг" + "</a>")
                elif id == vlad_id:
                    await message.reply("!Влад зассал ибо против него играют слишком сильные противники")
                    await message.client.send_message(1361873517, "Пидорас дня и по совместительству ссыкло - " + "<a href=\"tg://user?id=" + str(id) + "\">" + "Влад" + "</a>")
                else:
                    await message.client.send_message(-1001430533627, "!warn " + str(id) + " Лив из игры (Читать " + "<a href=\"https://t.me/rules_salieri/4\">Правила</a>)")
                    await message.client.send_message(1361873517, "<b>[Leave/Warn]</b>Выдал варн " + "<a href=\"tg://user?id=" + str(id) + "\">" + "пиздюку" + "</a>" + " ибо нехуй ливать с катки как последнее ссыкло")

        # except:
        #     pass

