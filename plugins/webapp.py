from pyrogram import filters
from pyrogram import Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrp = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Website", web_app_data="web_app"
                    ),
                ],
            ]
        )


@Client.on_message(filters.command("rsr", prefixes=["/", "!"]))
async def rsr(client, message):
  await client.send_message(message.chat.id, text="A hnuaia **Website** tih button khu hmet la min siamtu website i en thei ang.", reply_markup=rsrp, reply_to_message_id=message.id)
  return
