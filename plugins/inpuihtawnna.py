# ©️2022 RSR
from pyrogram import Client, filters

@Client.on_message(filters.chat(-1001465429519) & filters.new_chat_members)
async def inpuihtawnna(client, message):
    await client.send_message(-1001465429519, text=f"Hello {username},\n\n**{chatname}** group ah kan lo lawm a che. He group hi Telegram ani emaw thildang pawh nise i hriatloh i zawhna hmun tur ani e. Tin, i hriat zawng an lo zawh pawn tim miahlo in ilo chhang thei ang😊,Rules khu chhiar tur aw." reply_to_message_id=message.message_id)
