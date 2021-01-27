from .. import loader, utils
import time

messagepin = None
messagepin1 = None
sud_state = False


class ChsettingsMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'StgChanger'}

    async def sudnajacmd(self, event):
        """Вкл/выкл режим судной ночи"""
        global sud_state, messagepin, messagepin1
        x = await event.client.get_messages(1564155100, 3)
        if x[0].text == "1":
            sud_state = True
        elif x[0].text == "0":
            sud_state = False

        if not sud_state:
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
        """кто прочитал тот воскресе"""
        global sud_state
        x = await message.client.get_messages(1564155100, 3)
        if x[0].text == "1":
            sud_state = True
        elif x[0].text == "0":
            sud_state = False
        if 'параметры' in message.text.split():
            if sud_state:
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 enable_buffs')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 enable_buffs set_state True')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 hidden_voting')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 hidden_voting set_state True')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 show_roles')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 show_roles set_state True')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 friendly_fire')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 friendly_fire set_state False')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 kattani_first_night_shot')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 kattani_first_night_shot set_state False')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 main')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 exit')
                time.sleep(0.6)
                await x[0].edit("0")
                await message.client.send_message(-1001430533627, "<b>Настройки изменены. Можно играть!</b>")
            else:
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 enable_buffs')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 enable_buffs set_state False')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 hidden_voting')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 hidden_voting set_state False')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 show_roles')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 show_roles set_state False')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 friendly_fire')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 friendly_fire set_state True')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 kattani_first_night_shot')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 kattani_first_night_shot set_state True')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 misc')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 main')
                time.sleep(0.6)
                await message.click(data=b'config -1001430533627 exit')
                time.sleep(0.6)
                await x[0].edit("1")
                await message.client.send_message(-1001430533627, "<b>Настройки изменены. Можно играть!</b>")