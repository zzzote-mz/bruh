from pyrogram import Client, filters, enums





@Client.on_message(filters.command("id", prefixes=["/", "!"]))
async def identity(client, message):
    if message.reply_to_message and message.reply_to_message.forward_from:
        user1 = message.reply_to_message.from_user
        user2 = message.reply_to_message.forward_from
        await client.send_message(
          message.chat.id,
          text=f"**{user1.mention} ID:** `{user1.id}`\n**{user2.mention} ID:** `{user2.id}`",
          reply_to_message_id=message.id
        )
        return
    if message.reply_to_message.chat.type == enums.ChatType.CHANNEL:
        chan = message.reply_to_message.forward_from_chat
        await client.send_message(
          message.chat.id,
          text=f"**{chan.title} ID: `{chan.id}`",
          reply_to_message_id=message.id
        )
        return
    if not message.reply_to_message and len(message.command) == 1:
         user = message.from_user
         await client.send_message(
           message.chat.id,
           text=f"**{user.mention} ID:** `{user.id}`",
           reply_to_message_id=message.id
         )
         return
    if len(message.command) == 2:
         userq = message.text.split(None, 1)[1]
         userqs = await client.get_users(userq)
         await client.send_message(
           message.chat.id,
           text=f"**{userqs.mention} ID:** `{userqs.id}`",
           reply_to_message_id=message.id
         )
         return
