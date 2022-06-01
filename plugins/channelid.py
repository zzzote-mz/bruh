from pyrogram import Client, filters


@Client.on_message(filters.command("chid", prefixes=["/", "!"]))
async def channelid(client, message):
    if not message.reply_to_message:
        await client.send_message(
          message.chat.id,
          text="Channel message rawn forward la, chu chu command hian reply rawh",
          reply_to_message_id=message.id
        )
    else:
        test = f"**{message.reply_to_message.forward_from_chat.title} ID:** `{message.reply_to_message.forward_from_chat.id}`"
        await client.send_message(
          message.chat.id,
          text=test,
          reply_to_message_id=message.id
        )
