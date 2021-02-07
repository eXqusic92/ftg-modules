from .. import loader, utils
from telethon import events
import asyncio

messagepin = None
messagepin1 = None

class ChsettingsMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'StgChanger'}

    async def client_ready(self, client, db):
        self._db = db

    async def sudnajacmd(self, event):
        """Вкл/выкл режим судной ночи"""
        global messagepin, messagepin1

        sud_state = self._db.get("sud_settings", "state")
        chat = '@TrueMafiaBlackBot'
        async with event.client.conversation(chat) as conv:
            if not sud_state:
                messagepin = await event.client.send_message(-1001430533627, "<b>!Судная ночь началась!!! Сейчас никакие правила не действуют!!!</b>")
                if messagepin1:
                    await messagepin1.delete()
                await messagepin.pin()
                await event.client.send_message(-1001430533627, "<b>Меняю настройки игры... Не начинайте игру в ближайшие 30 секунд</b>")
                await asyncio.sleep(2)
                await event.client.send_message(-1001430533627, "/cancel")
                await asyncio.sleep(0.5)
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1564155100))
                await event.client.send_message(-1001430533627, "/settings@TrueMafiaBlackBot")
                response = await response
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 enable_buffs')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 enable_buffs set_state False')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 hidden_voting')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 hidden_voting set_state False')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 show_roles')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 show_roles set_state False')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 friendly_fire')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 friendly_fire set_state True')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 kattani_first_night_shot')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 kattani_first_night_shot set_state True')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 main')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 exit')
                await asyncio.sleep(0.6)
                self._db.set("sud_settings", "state", True)
                await event.client.send_message(-1001430533627, "<b>Настройки изменены. Можно играть!</b>")
                await asyncio.sleep(0.5)
                await event.client.send_message(-1001430533627, "/game@TrueMafiaBlackBot")
                await asyncio.sleep(0.5)
                await event.client.send_message(-1001430533627, "анрег")

            else:
                messagepin1 = await event.client.send_message(-1001430533627, "<b>!Режим судной ночи окончен!! Правила снова действуют</b>")
                if messagepin:
                    await messagepin.delete()
                await messagepin1.pin()
                await event.client.send_message(-1001430533627, "<b>Меняю настройки игры... Не начинайте игру в ближайшие 30 секунд</b>")
                await asyncio.sleep(2)
                await event.client.send_message(-1001430533627, "/cancel")
                await asyncio.sleep(0.5)
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1564155100))
                await event.client.send_message(-1001430533627, "/settings@TrueMafiaBlackBot")
                response = await response
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 enable_buffs')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 enable_buffs set_state True')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 hidden_voting')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 hidden_voting set_state True')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 show_roles')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 show_roles set_state True')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 friendly_fire')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 friendly_fire set_state False')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 kattani_first_night_shot')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 kattani_first_night_shot set_state False')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 misc')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 main')
                await asyncio.sleep(0.6)
                await response.click(data=b'config -1001430533627 exit')
                await asyncio.sleep(0.6)
                self._db.set("sud_settings", "state", False)
                await event.client.send_message(-1001430533627, "<b>Настройки изменены. Можно играть!</b>")
                await asyncio.sleep(0.5)
                await event.client.send_message(-1001430533627, "/game@TrueMafiaBlackBot")
                await asyncio.sleep(0.5)
                await event.client.send_message(-1001430533627, "анрег")
