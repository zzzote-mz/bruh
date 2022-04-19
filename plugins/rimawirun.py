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
                        "Mizo Bots Talk", url="http://t.me/mizobotstalk"
                    ),
                    InlineKeyboardButton(
                        "Mizo Bot Store 👨‍🔧", url="https://t.me/mizobotstore"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Mizo Library", url="https://t.me/mizolibrary"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001167470612) & filters.new_chat_members)
async def rimawirun(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001167470612, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah kan lo lawm a che, hemi group a hla download dan i hriat duh chuan a hnuai button a **Tutorial 1** leh **Tutorial 2** tih khu hmet la i en dawn nia, a 2 khan a hman theih ve ve avangin a 2 khan i en dawn nia.\n\nGroup awm nuam le.", reply_markup=rsrke, reply_to_message_id=message.message_id)
          return
