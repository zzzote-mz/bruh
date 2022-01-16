from pyrogram import filters
from pyrogram import Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton






rsrk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Tutorial", url="https://youtu.be/1jhYo0ugBTw"
                    )
                ],
            ]
        )

@Client.on_message(filters.command('tutorial'))
async def tutorial(client, message):
  await client.send_message(message.chat.id, text="A hnuaia **Tutorial** tih button khu hmet la, video kha uluk deuh in en zo rawh, kha kha min hman dan hrilhfiahna video ani.", reply_markup=rsrk, reply_to_message_id=message.message_id)
    
        
