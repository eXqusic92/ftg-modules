from .. import loader, utils


class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием GroupHelpBot"""
    strings = {'name': 'tst'}

    async def client_ready(self, client):
        """Вкл/выкл автоварн"""
        self.client = client
        await self.client.send_message('me', 'ky')
