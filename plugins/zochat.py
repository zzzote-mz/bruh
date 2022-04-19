# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Rules", url="https://telegra.ph/Rules-04-19-6"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Invite Friends", url="https://t.me/share/url?url=https://t.me/joinchat/CMdvPb-0ZEFjOTg1"
                    ),
                    InlineKeyboardButton(
                        "Bot Helpline", url="https://t.me/helptereuhte"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001227426454) & filters.new_chat_members)
async def zochat(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001227426454, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah kan lo lawm a che, he group hi inkawm hlimna group ani e, description chhiar tur aw, chuan rilru te tit tet put loh tur he group ah hian.\n\nI hmel hi a chhia chu ka tilo anga mahse, i hmel kha a tlo hmel🤓", reply_markup=rsrke, reply_to_message_id=message.message_id)
          return
