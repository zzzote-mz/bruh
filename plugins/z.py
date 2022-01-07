import asyncio
from pyrogram import Client, filters
from utils import is_subscribed


@Client.on_message(filters.private & filters.text)
async def nor(client, message):
    if not await is_subscribed(client, message):
        await client.send_message(
            message.chat.id,
            text="Min hman duh chuan a hnuaia **Join** tih button hi hmet la join rawh, channel member te chauh in min hmang thei.",
            reply_to_message_id=message.message_id,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return
    await client.send_message(
        message.chat.id,
        text="**i thil zawn hi ka ka hmuzo miahlo mai, ka database ah a awmlo emaw i search dan a fuh tawklo ani maithei ani.**",
        reply_to_message_id=message.message_id
    )
