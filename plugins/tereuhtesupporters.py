# ©️2022 RSR
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Gpay", url="https://telegra.ph/%F0%9D%9A%81%F0%9D%9A%82%F0%9D%9A%81-06-19"
                    ),
                    InlineKeyboardButton(
                        "Bank", url="https://telegra.ph/%F0%9D%9A%81%F0%9D%9A%82%F0%9D%9A%81-09-06"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Paypal", url="https://paypal.me/rickyzote"
                    ),
                    InlineKeyboardButton(
                        "Beer", url="https://www.buymeacoffee.com/rsrmusic"
                    ),
                ],
            ]
        )

@Client.on_message(filters.chat(-1001231244897) & filters.new_chat_members)
async def supporters(client, message):
    for rsr in message.new_chat_members:
          await client.send_message(-1001231244897, text=f"Hello {rsr.mention}\n\n**{message.chat.title}** group ah hian kan lo lawm a che. Donate dan tur i hriatloh chuan #donate 👈tiang hian group ah hian ilo thawn dawn nia, i donate anih chuan i donate zawh ah i donate ani tih hriatna tur khan screenshot la, group ah hian ilo dah dawn nia i screenshot kha.\n\nHun hman nuam le😊", reply_to_message_id=message.message_id)
          return
        
        
@Client.on_message(filters.command("donate", prefixes=["#"]) & filters.chat(-1001231244897))
async def donatecom(client, message):
    await client.send_message(-1001231244897, text="Donate i duh chuan a hnuaia button ho ah khuan i donate theihna/duhna kha click mai rawh aw, i click zawh ah open ngai chi anih chuan i open leh mai dawn nia.", reply_markup=rsrke, reply_to_message_id=message.message_id)
    return
