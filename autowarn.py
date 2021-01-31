from .. import loader, utils
import time

messagepin = None
messagepin1 = None
sud_state = False

class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'AutoWarn'}

    async def turncmd(self, event):
        """Вкл/выкл автоварн"""
        global sud_state
        if sud_state:
            sud_state = False
            await event.respond("<b>Автоварн включен</b>")
            time.sleep(0.2)
            await event.respond("анрег")
        else:
            sud_state = True
            await event.respond("<b>Автоварн выключен</b>")
            time.sleep(0.2)
            await event.respond("анрег")

    async def watcher(self, message):
        """почему это называется watcher???"""
        global sud_state

        admin_ids = [540902565, 883140642, 491255683, 198119497, 895755815, 725431547, 690394127, 1106663428]
        souch_ids = [1564155100, 504225012]
        vlad_id = 508169464
        if not sud_state:
            uid = message.entities[0].user_id
            userent = await message.client.get_entity(uid)
            if userent.last_name is None:
                username = str(userent.first_name)
            elif userent.last_name and userent.first_name:
                username = str(userent.first_name) + " " + str(userent.last_name)
            else:
                username = str(userent.last_name)
            chatid = message.chat_id
            fromid = message.from_id

            if chatid == -1001430533627 and fromid == 761250017:
                if 'бу-у-у-у-ду' in message.raw_text.split():
                    if uid in admin_ids:
                        await message.reply("!Вот петушара, админ, ещё и АФКшит...")
                        await message.client.send_message(1361873517, "<a href=\"tg://user?id=" + str(uid) + "\">" + username + "</a>" + " сидит в афк псина")
                        time.sleep(0.2)
                        await message.respond("анрег")
                    elif uid in souch_ids:
                        await message.reply("!Уважаю")
                        await message.client.send_message(1361873517, "Респект и уважение этому человеку " + "<a href=\"tg://user?id=" + str(uid) + "\">" + username + "</a>")
                        time.sleep(0.2)
                        await message.respond("анрег")
                    elif uid == vlad_id:
                        await message.reply("!Блядь, я тебя захуярю")
                        await message.client.send_message(1361873517, "Блять" + "<a href=\"tg://user?id=" + str(uid) + "\">" + "Влад" + "</a>" + " хули ты сам сидишь и дрочеш в группе, а на других орёшь что они афк? А?А?А?А?")
                        time.sleep(0.2)
                        await message.respond("анрег")
                    else:
                        await message.client.send_message(-1001430533627, "!warn " + str(uid) + " AFK (Читать " + "<a href=\"https://t.me/rules_salieri/14\">Правила</a>)")
                        await message.client.send_message(1361873517, "<b>[AFK/Warn] </b>Выдал варн " + "<a href=\"tg://user?id=" + str(uid) + "\">" + username + "</a>" + " ибо нехуй сидеть в афк")
                        time.sleep(0.2)
                        await message.respond("анрег")

                if 'гнетущей' in message.raw_text.split():
                    if userent.last_name is None:
                        username = str(userent.first_name)
                    elif userent.last_name and userent.first_name:
                        username = str(userent.first_name) + " " + str(userent.last_name)
                    else:
                        username = str(userent.last_name)
                    if uid in admin_ids:
                        await message.reply("!Нахуй ливаешь, долбоёб?")
                        await message.client.send_message(1361873517, "Ало " + "<a href=\"tg://user?id=" + str(uid) + "\">" + username + "</a>" + " ты зашёл в катку чтобы повыпендриваться? Так сиди до конца, а не ливай посреди катки как крыса.")
                        time.sleep(0.2)
                        await message.respond("анрег")
                    elif uid in souch_ids:
                        await message.reply("!Ну и пошёл нахуй отсюдава")
                        await message.client.send_message(1361873517, "Ммм.. Хорошая попытка сбежать, " + "<a href=\"tg://user?id=" + str(uid) + "\">" + username + "</a>")
                        time.sleep(0.2)
                        await message.respond("анрег")
                    elif uid == vlad_id:
                        await message.reply("!Влад зассал ибо против него играют слишком сильные противники")
                        await message.client.send_message(1361873517, "Krasav4ik - " + "<a href=\"tg://user?id=" + str(uid) + "\">" + "Влад" + "</a>")
                        time.sleep(0.2)
                        await message.respond("анрег")
                    else:
                        await message.client.send_message(-1001430533627, "!warn " + str(uid) + " Лив из игры (Читать " + "<a href=\"https://t.me/rules_salieri/14\">Правила</a>)")
                        await message.client.send_message(1361873517, "<b>[Leave/Warn] </b>Выдал варн " + "<a href=\"tg://user?id=" + str(uid) + "\">" + username + "</a>" + " ибо нехуй ливать с катки как последнее ссыкло")

