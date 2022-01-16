from pyrogram import filters
from pyrogram import Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




rsr = "BAACAgUAAx0CQyM-SQACYPlh44T_DSbmmYDBUUq7lyIcDrxd1AAC1AMAAsuTMVWli90iL0SkKiME"

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
  await client.send_photo(message.chat.id, photo=rsr, caption="**A hnuaia button ho khu min siamtu biak pawh theihna te ani e.**", reply_markup=rsrk, reply_to_message_id=message.message_id)
    
        
