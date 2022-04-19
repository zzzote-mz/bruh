# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Hriat tûr", url="https://t.me/mzbotstalk/79"
                    ),
                    InlineKeyboardButton(
                        "Bot List", url="https://t.me/mzbotstalk/70"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Submit", url="https://t.me/mzsubbot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Mizo Bot Store", url="https://t.me/mizobotstore"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001713059419) & filters.new_chat_members)
async def mizobotstalk(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001713059419, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah kan lo lawm a che. Hetah hian i Telegram Bot hman duh leh nangma Bot emaw Bot dang chungchang i sawi thei ang, **Hriat tûr** khu chhiar tur aw, chuan **Bot List** khu Bot submit tawh ho list en na ani. Chuan, **Submit** tih aṭang khuan i Bot siam i submit ve thei ang.", reply_markup=rsrke, reply_to_message_id=message.message_id)
          return
