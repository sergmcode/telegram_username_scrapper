
from app_configuration import api_id, api_hash, phone

from telethon import TelegramClient, events
client = TelegramClient('anon', api_id, api_hash)

import json

async def main():
    # Getting information about yourself
    # me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID
    # await client.send_message(-1001114423954, 'Hello!')
    # ...to your contacts
    # await client.send_message('+34600123123', 'Hello!')
    # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '~/me.jpg')

    # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)

    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

    # print(await client.get_participants("@sergiotgroup"))
    usernames = []
    async for p in client.iter_participants("@higher_math"):
        # print(p.id, p.username)
        usernames.append(p.username)
    with open("users.json", 'w') as f:
        json.dump(usernames, f)
    pass

with client:
    client.loop.run_until_complete(main())

# from telethon import TelegramClient, events

# client = TelegramClient('anon', api_id, api_hash)

# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     if 'hello' in event.raw_text:
#         await event.reply('hi!')

# client.start()
# client.run_until_disconnected()