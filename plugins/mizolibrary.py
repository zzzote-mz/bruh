# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Rules", url="https://telegra.ph/Rules-03-06-6"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001256541031) & filters.new_chat_members)
async def mizolibrary(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001256541031, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah hian kan lo lawm a che. He group hi Story leh a rem rem post na tura siam ania, chutihrual chuan post tur i neih chuan post mawl tawp lovin @rsrmusic hnen ah hian i post tur kha enge ani tih iva hrilh phawt dawn nia, post tawp kan phalloh chhan hi fake leh thil thalo post a awm loh na'n ani e, hun hman nuam le😊", reply_markup=rsrke, reply_to_message_id=message.id)
          return
