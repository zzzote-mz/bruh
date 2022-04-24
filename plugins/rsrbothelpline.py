# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Rules", url="https://telegra.ph/Rules-04-19-5"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Chat Group", url="https://t.me/zochating"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/rsrbots"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Mizo Bots Talk", url="https://t.me/mzbotstalk"
                    ),
                    InlineKeyboardButton(
                        "Mizo Bot Store", url="https://t.me/mizobotstore"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Mizo Library", url="https://t.me/mizolibrary"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001400522942) & filters.new_chat_members)
async def rsrbothelpline(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001400522942, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah kan lo lawm a che, he group hi RSR Bot siam a felhlelh awm leh a hman dan zirna hmun ani e, chuan **Rules** tih khu chhiar tur aw, hetah nawi lutuk a rem loh avangin nawi duh tan **Chat Group** tih khu join leh mai tur, **Channel** tih khu Join/Follow ve bawk rawh aw.", reply_markup=rsrke, reply_to_message_id=message.id)
          return
