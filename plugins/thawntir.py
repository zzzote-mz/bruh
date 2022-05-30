# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status


@Client.on_message(filters.command("tlangvalte", prefixes=["/", "!"]) & filters.group)
async def thawntir(client, message):
  heh = message.from_user.id
  huh = await message.chat.get_member(heh)
  if not huh.status in admin_status:
      return await message.reply_text(
          "Admin i nih loh chuan i ti ve theilo."
      )
  if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command zawh ah min thawn tir tur dah la thawn rawh. Emaw, command hmang hian message reply rawh.**")
       return
  elif message.reply_to_message:
     await client.copy_message(
       chat_id=message.chat.id,
       from_chat_id= message.chat.id,
       message_id=message.reply_to_message.id
     )
     await client.delete_messages(
       message.chat.id,
       message.reply_to_message.id
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
  
     
