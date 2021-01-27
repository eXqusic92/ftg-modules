from .. import loader, utils
import time

sud_state = False


class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'Stg'}

    async def msgcmd(self, event):
        """Вкл/выкл режим судной ночи"""
        pass

    async def watcher(self, message):
        """кто прочитал тот воскресе"""
        global sud_state
        x = await message.client.get_messages(1564155100, 3)
        if x[0].text == "1":
            sud_state = True
        elif x[0].text == "0":
            sud_state = False
        from_id = message.from_id
        if 'хотите' in message.raw_text.split() and 'изменить' in message.raw_text.split():
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