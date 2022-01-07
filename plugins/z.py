import asyncio
from pyrogram import Client, filters
from plugins.fsub import ForceSub
from database.adduser import AddUser


@Client.on_message(filters.private & filters.text)
async def nor(client, message):
    await AddUser(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await client.send_message(
        message.chat.id,
        text="**i thil zawn hi ka ka hmuzo miahlo mai, ka database ah a awmlo emaw i search dan a fuh tawklo ani maithei ani.**",
        reply_to_message_id=message.message_id
    )
