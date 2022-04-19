# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Hrilhfiahna", url="https://youtu.be/0nSqM7MPpLo"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Rate", url="https://telegra.ph/Bot-Rate-02-13"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001775992978) & filters.new_chat_members)
async def mizobotstore(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001775992978, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah hian kan lo lawm a che. He group hi i pual a Telegram Bot i neih ve theih na'n Bot i leina hmun tur atana siam ani. Bot lei awmzia leh tihdan i hriatloh chuan a hnuaia **Hrilhfiahna** tih button hi hmet la en rawh uluk deuh in, chuan Bot siam man hi i en duh chuan a hnuai button ah tho khuan **Rate** tih button khu hmet la i en thei ang.", reply_markup=rsrke, reply_to_message_id=message.message_id)
          return
