from .. import loader, utils


@loader.tds
class WelcomeMod(loader.Module):
    """Приветствие новых пользователей в чате."""
    strings = {'name': 'Welcome'}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def welcomecmd(self, message):
        """Включить/выключить приветствие новых пользователей в чате. Используй: .welcome <clearall (по желанию)>."""
        welcome = self.db.get("Welcome", "welcome", {})
        chatid = str(message.chat_id)
        args = utils.get_args_raw(message)
        if args == "clearall":
            self.db.set("Welcome", "welcome", {})
            return await message.edit("<b>[Welcome Mode]</b> Все настройки модуля сброшены.")

        if chatid in welcome:
            welcome.pop(chatid)
            self.db.set("Welcome", "welcome", welcome)
            return await message.edit("<b>[Welcome Mode]</b> Деактивирован!")

        welcome.setdefault(chatid, {})
        welcome[chatid].setdefault("message", "Добро пожаловать в чат!")
        welcome[chatid].setdefault("is_reply", False)
        self.db.set("Welcome", "welcome", welcome)
        await message.edit("<b>[Welcome Mode]</b> Активирован!")


    async def setwelcomecmd(self, message):
        """Установить новое приветствие новых пользователей в чате.\nИспользуй: .setwelcome <текст (можно использовать {name}; {chat})>; ничего."""
        welcome = self.db.get("Welcome", "welcome", {})
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        chatid = str(message.chat_id)
        chat = await message.client.get_entity(int(chatid))
        try:
            if not args and not reply:
                return await message.edit(f'<b>Приветствие новых пользователей в "{chat.title}":</b>\n\n'
                                          f'<b>Статус:</b> Включено.\n'
                                          f'<b>Приветствие:</b> {welcome[chatid]["message"]}\n\n'
                                          f'<b>~ Установить новое приветствие можно с помощью команды:</b> .setwelcome <текст>.')
            else:
                if reply:
                    welcome[chatid]["message"] = reply.id
                    welcome[chatid]["is_reply"] = True
                else:
                    welcome[chatid]["message"] = args
                    welcome[chatid]["is_reply"] = False
                self.db.set("Welcome", "welcome", welcome)
                return await message.edit("<b>Новое приветствие установлено успешно!</b>")
        except KeyError: return await message.edit(f'<b>Приветствие новых пользователей в "{chat.title}":</b>\n\n'
                                                   f'<b>Статус:</b> Отключено')


    async def watcher(self, message):
        """че за хуйня блять"""
        try:
            if message.chat_id == -1001430533627 and message.from_id == 761250017:
                txt = message.text
                if 'бу-у-у-у-ду' in txt.split():
                    message.client.send_message('me', "test")
        except:
            pass