# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("warn", prefixes=["/", "!"]) & filters.group)
@admins_only
async def warn(client, message):
    if message.reply_to_message:
        idu = message.text.split(None, 1)[1]
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {umen}\n**➥ID:** {uid}", reply_to_message_id=message.reply_to_message.message_id)
        return
    else:
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.ban_chat_member(message.chat.id, user_id=idu)
        await client.send_message(message.chat.id, text=f"{umens} hi Ban ani e.", reply_to_message_id=message.message_id)
        return
