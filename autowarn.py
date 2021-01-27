from .. import loader, utils
import time

messagepin = None
messagepin1 = None
sud_state = False

class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'AutoWarn'}

    async def sudnajacmd(self, event):
        """Вкл/выкл режим судной ночи"""
        global sud_state, messagepin, messagepin1
        x = await event.client.get_messages(1564155100, 3)
        if x[0].text == "1":
            sud_state = True
        elif x[0].text == "0":
            sud_state = False

        if sud_state:
            messagepin = await event.client.send_message(-1001430533627, "<b>!Судная ночь началась!!! Сейчас никакие правила не действуют!!!</b>")
            if messagepin1:
                await messagepin1.delete()
            await messagepin.pin()
            await event.client.send_message(-1001430533627, "<b>Меняю настройки игры... Не начинайте игру в ближайшие 30 секунд</b>")
            time.sleep(2)
            await event.client.send_message(-1001430533627, "/cancel")
            time.sleep(0.5)
            await event.client.send_message(-1001430533627, "/settings@TrueMafiaBlackBot")
        else:
            messagepin1 = await event.client.send_message(-1001430533627, "<b>!Режим судной ночи окончен!! Правила снова действуют</b>")
            if messagepin:
                await messagepin.delete()
            await messagepin1.pin()
            await event.client.send_message(-1001430533627, "<b>Меняю настройки игры... Не начинайте игру в ближайшие 30 секунд</b>")
            time.sleep(2)
            await event.client.send_message(-1001430533627, "/cancel")
            time.sleep(0.5)
            await event.client.send_message(-1001430533627, "/settings@TrueMafiaBlackBot")

    async def watcher(self, message):
        """почему это называется watcher???"""
        global sud_state
        admin_ids = [725431547, 895755815, 540902565, 883140642, 754756140, 491255683, 1001187772, 198119497, 890602515, 662737931]
        souch_ids = [1564155100, 504225012]
        vlad_id = 508169464
        if not sud_state:
            text = message.text.split("=")
            r = text[2].split('"')
            id = int(r[0])
            userent = await message.client.get_entity(id)
            if userent.last_name is None:
                username = str(userent.first_name)
            elif userent.last_name and userent.first_name:
                username = str(userent.first_name) + " " + str(userent.last_name)
            else:
                username = str(userent.last_name)
            chatid = message.chat_id
            msgtxt = str(message.text)
            fromid = message.from_id

            if chatid == -1001430533627 and fromid == 761250017:
                if 'бу-у-у-у-ду' in message.raw_text.split():
                    if id in admin_ids:
                        await message.reply("!Вот петушара, админ, ещё и АФКшит...")
                        await message.client.send_message(1361873517, "<a href=\"tg://user?id=" + str(id) + "\">" + username + "</a>" + " сидит в афк псина")
                    elif id in souch_ids:
                        await message.reply("!Уважаю")
                        await message.client.send_message(1361873517, "Респект и уважение этому человеку " + "<a href=\"tg://user?id=" + str(id) + "\">" + username + "</a>")
                    elif id == vlad_id:
                        await message.reply("!Блядь, я тебя захуярю")
                        await message.client.send_message(1361873517, "Блять" + "<a href=\"tg://user?id=" + str(id) + "\">" + "Влад" + "</a>" + " хули ты сам сидишь и дрочеш в группе, а на других орёшь что они афк? А?А?А?А?")
                    else:
                        await message.client.send_message(-1001430533627, "!warn " + str(id) + " AFK (Читать " + "<a href=\"https://t.me/rules_salieri/14\">Правила</a>)")
                        await message.client.send_message(1361873517, "<b>[AFK/Warn] </b>Выдал варн " + "<a href=\"tg://user?id=" + str(id) + "\">" + username + "</a>" + " ибо нехуй сидеть в афк")

                if 'гнетущей' in message.raw_text.split():
                    str1 = message.text.split("\"")
                    id = int(str1[1].strip("tg://user?id="))
                    if userent.last_name is None:
                        username = str(userent.first_name)
                    elif userent.last_name and userent.first_name:
                        username = str(userent.first_name) + " " + str(userent.last_name)
                    else:
                        username = str(userent.last_name)
                    if id in admin_ids:
                        await message.reply("!Нахуй ливаешь, долбоёб?")
                        await message.client.send_message(1361873517, "Ало " + "<a href=\"tg://user?id=" + str(id) + "\">" + username + "</a>" + " ты зашёл в катку чтобы повыпендриваться? Так сиди до конца, а не ливай посреди катки как крыса.")
                    elif id in souch_ids:
                        await message.reply("!Ну и пошёл нахуй отсюдава")
                        await message.client.send_message(1361873517, "Ммм.. Хорошая попытка сбежать, " + "<a href=\"tg://user?id=" + str(id) + "\">" + username + "</a>")
                    elif id == vlad_id:
                        await message.reply("!Влад зассал ибо против него играют слишком сильные противники")
                        await message.client.send_message(1361873517, "Krasav4ik - " + "<a href=\"tg://user?id=" + str(id) + "\">" + "Влад" + "</a>")
                    else:
                        await message.client.send_message(-1001430533627, "!warn " + str(id) + " Лив из игры (Читать " + "<a href=\"https://t.me/rules_salieri/14\">Правила</a>)")
                        await message.client.send_message(1361873517, "<b>[Leave/Warn] </b>Выдал варн " + "<a href=\"tg://user?id=" + str(id) + "\">" + username + "</a>" + " ибо нехуй ливать с катки как последнее ссыкло")

