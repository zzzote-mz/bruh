#©️ 2022 RSR

from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status


@Client.on_message(filters.command("protect", prefixes=["/", "!"]) & filters.group)
async def protect(client, message):
  heh = message.from_user.id
  huh = await message.chat.get_member(heh)
  if not huh.status in admin_status:
      return await message.reply_text(
          "Admin i nih loh chuan i ti ve theilo."
      )
  if message.reply_to_message:
     await client.copy_message(
       chat_id=message.chat.id,
       from_chat_id= message.chat.id,
       message_id=message.reply_to_message.id,
       protect_content=True
     )
     await client.delete_messages(
       message.chat.id,
       message.reply_to_message.id
     )
     await message.delete()
  else:
       await client.send_message(
         message.chat.id,
         text="**Message reply rawh.**",
         reply_to_message_id=message.id
       )
  
     
