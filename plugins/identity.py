from pyrogram import Client, filters, enums
from Tereuhte.tetakte.admins import group_types




@Client.on_message(filters.command("id", prefixes=["/", "!"]))
async def identity(client, message):
    if len(message.command) == 2:
         userq = message.text.split(None, 1)[1]
         userqs = await client.get_users(userq)
         await client.send_message(
           message.chat.id,
           text=f"**{userqs.mention} ID:** `{userqs.id}`",
           reply_to_message_id=message.id
         )
         return
    elif message.reply_to_message:
        user1 = message.from_user
        user2 = message.reply_to_message.from_user
        await client.send_message(
          message.chat.id,
          text=f"**{user1.mention} ID:** `{user1.id}`\n**{user2.mention} ID:** `{user2.id}`",
          reply_to_message_id=message.id
        )
        return
    elif message.reply_to_message.forward_from:
        user1 = message.reply_to_message.forward_from_chat
        user2 = message.reply_to_message.forward_from
        await client.send_message(
          message.chat.id,
          text=f"**{user2.mention} ID:** `{user2.id}`\n**{user1.title} ID:** `{user1.id}`",
          reply_to_message_id=message.id
        )
        return
    elif not message.reply_to_message and message.chat.type in group_types:
        chan = message.chat
        user = message.from_user
        await client.send_message(
          message.chat.id,
          text=f"**{user.mention} ID:** `{user.id}`\n**Group ID:** `{chan.id}`",
          reply_to_message_id=message.id
        )
        return
    elif not message.reply_to_message and message.chat.type == enums.ChatType.PRIVATE:
         user = message.from_user
         await client.send_message(
           message.chat.id,
           text=f"**{user.mention} ID:** `{user.id}`",
           reply_to_message_id=message.id
         )
         return
    
