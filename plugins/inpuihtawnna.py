# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Bot Helpline 🤖", url="https://t.me/helptereuhte"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Channel 🔔", url="https://t.me/rsrbots"
                    ),
                    InlineKeyboardButton(
                        "Chat Group 👾", url="https://t.me/zochating"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Invite Friends 👥", url="http://t.me/share/url?url=https://t.me/rsrtginfo"
                    ),
                    InlineKeyboardButton(
                        "Mizo Bot Store 👨‍🔧", url="https://t.me/mizobotstore"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Rules ❗", url="https://telegra.ph/Rules-04-19-5"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001465429519) & filters.new_chat_members)
async def inpuihtawnna(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001465429519, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah kan lo lawm a che. He group hi Telegram ani emaw thildang pawh nise i hriatloh i zawhna hmun tur ani e. Tin, i hriat zawng an lo zawh pawn tim miahlo in ilo chhang thei ang😊, Rules khu chhiar tur aw.", reply_markup=rsrke, reply_to_message_id=message.id)
          return
