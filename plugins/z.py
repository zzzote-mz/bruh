import asyncio
from pyrogram import Client, filters



@Client.on_message(filters.private & filters.text)
async def nor(client, message):
    await AddUser(client, message)
    await client.send_message(
        message.chat.id,
        text="**i thil zawn hi ka ka hmuzo miahlo mai, ka database ah a awmlo emaw i search dan a fuh tawklo ani maithei ani.**",
        reply_to_message_id=message.message_id
    )
