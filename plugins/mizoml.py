# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Invite Friends", url="https://t.me/share/url?url=Mizo%20Mobile%20Legend%20khel%20%E1%B9%ADhin%20te%20tan%20group%20siam%20ania%2C%20i%20khel%20ve%20a%2C%20i%20join%20ve%20duh%20anih%20chuan%20a%20hnuai%20a%20join%20tia%20ka%20kawh%20na%20a%20username%20khu%20click%20in%20i%20join%20thei%20ang.%0A%0AJoin%20%F0%9F%91%89%20%40mizoml"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001625845943) & filters.new_chat_members)
async def mizoml(client, message):
    for rsr in message.new_chat_members:
          await client.send_video(-1001625845943, video="https://telegra.ph/file/d53ad20d816189453d751.mp4", caption=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah hian kan lo lawm a che😘", reply_markup=rsrke, reply_to_message_id=message.message_id)
          return
