# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("tereuhte", prefixes=["/", "!"]) & filters.group)
@admins_only
async def thawntir(client, message):
  if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command zawh ah min thawn tir tur dah la thawn rawh. Emaw, command hmang hian message reply rawh.**")
       return
  elif message.reply_to_message:
     await client.copy_message(
       chat_id=message.chat.id,
       from_chat_id= message.chat.id,
       message_id=message.reply_to_message.message_id
     )
     await client.delete_messages(
       message.chat.id,
       message.reply_to_message.message_id
     )
     await message.delete()
  else:
       ricky = message.text.split(None, 1)[1]
       await client.send_message(
         message.chat.id,
         text=ricky,
         disable_web_page_preview=True
       )
       await message.delete()
  
     
