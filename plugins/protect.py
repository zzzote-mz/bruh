#©️ 2022 RSR

from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("protect", prefixes=["/", "!"]) & filters.group)
@admins_only
async def protect(client, message):
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
  
     
