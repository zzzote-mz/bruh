# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.chat(-1001374152167) & filters.new_chat_members)
async def lab(client, message):
    for rsr in message.new_chat_members:
          await client.send_animation(-1001374152167, animation="CgACAgQAAx0EUefl5wACAjNiXtfr03Itt4aY1mo-S6r1Pvpj7gACSQIAAiE9rVLZk2BzMLho7CQE", caption=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah hian kan lo lawm a che🤓", reply_to_message_id=message.id)
          return
