from pyrogram import Client, filters



@Client.on_message(filters.group & filters.command("msg", prefixes=["/", "!"]))
async def msg(client, message):
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            text=f"He Group ah hian message `{message.id}` thawn ani tawh.",
            reply_to_message_id=message.reply_to_message.id
        )
    else:
        await client.send_message(
            message.chat.id,
            text=f"He Group ah hian message `{message.id}` thawn ani tawh.",
            reply_to_message_id=message.id
        )
        
