from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 28509031
api_hash = '86a341f619e093b8b2168dad9844c0db'

# Login sử dụng session có sẵn
client = TelegramClient('anon', api_id, api_hash)

# The first parameter is the .session file name (absolute paths allowed)
# Đăng nhập vào acc Telegram, callback gửi tin nhắn đến acc của mình
# with TelegramClient('anon', api_id, api_hash) as client:
#     # Khởi động Telegram engine
#     client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

async def main():
     # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    await client.send_message('me', 'Hello, myself!')

with client:
    client.loop.run_until_complete(main())