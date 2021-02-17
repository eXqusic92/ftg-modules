import telethon
from telethon import TelegramClient
from telethon import events
api_id = 2196711
api_hash = '5668721b41aa4a8fbaa0b2939bb7960c'

client = TelegramClient('anon9', api_id, api_hash)


async def main():
    phone = '+34 123 123 123'
    name = "Test"
    sent = await client.send_code_request(phone)
    print(sent)
    code = input("Enter code: ")
    await client.start(phone=phone, force_sms=True, first_name=name, code_callback=code)

with client as client:
    client.loop.run_until_complete(main())