# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Tutorial 1", url="https://youtu.be/IGrQKIzcrL4"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Tutorial 2", url="https://youtu.be/3THNv0R3GO4"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Inpuih tawnna", url="https://t.me/rsrtginfo"
                    ),
                    InlineKeyboardButton(
                        "Story postna", url="https://t.me/storyhranghrangpostna"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Group link share na", url="https://t.me/grouplinkpostna"
                    ),
                    InlineKeyboardButton(
                        "Bot Helpline", url="https://t.me/helptereuhte"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Mizo Bot Store", url="https://t.me/mizobotstore"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001167470612) & filters.new_chat_members)
async def rimawirun(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001167470612, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah kan lo lawm a che, hemi group a hla download dan i hriat duh chuan a hnuai button a **Tutorial 1** leh **Tutorial 2** tih khu hmet la i en dawn nia, a 2 khan a hman theih ve ve avangin a 2 khan i en dawn nia.\n\nGroup awm nuam le.", reply_markup=rsrke, reply_to_message_id=message.id)
          return
