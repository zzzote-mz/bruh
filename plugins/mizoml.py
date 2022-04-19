# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Invite Friends", url="https://youtu.be/0nSqM7MPpLo"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001625845943) & filters.new_chat_members)
async def mizoml(client, message):
    for rsr in message.new_chat_members:
          await client.send_video(-1001625845943, video="https://telegra.ph/file/d53ad20d816189453d751.mp4", caption=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah hian kan lo lawm a che😘", reply_markup=rsrke, reply_to_message_id=message.message_id)
          return
