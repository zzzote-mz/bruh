from pyrogram import filters
from pyrogram import Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




rsr = "BAACAgUAAx0CSSkKlgABAQpkYY0PZg3eLFh8vbYk5ISabRV2f5sAAtQDAALLkzFVpYvdIi9EpCoiBA"

rsrk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Telegram", url="https://t.me/rsrmusic"
                    ),
                    InlineKeyboardButton(
                        "Whatsapp", url="https://wa.me/918974636370"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Website", url="www.imrsr.online"
                    )
                ],
            ]
        )

@Client.on_message(filters.command('creator'))
async def creator(client, message):
  await client.send_video(message.chat.id, rsr, caption="**A hnuaia button ho khu min siamtu biak pawh theihna te ani e.**", reply_markup=rsrk, reply_to_message_id=message.message_id)
    
        
