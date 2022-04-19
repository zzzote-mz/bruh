# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("ban", prefixes=["/", "!"]))
@admins_only
async def ban(client, message):
    if not 5301276537.status == "administrator":
        await client.send_message(message.chat.id, text="Admin ka nilo, chuvang chuan hetah tumah ka ban theilo.", reply_to_message_id=message.message_id)
        return
    elif message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.ban_chat_member(message.chat.id, user_id=uid)
        await client.send_message(message.chat.id, text=f"{umen} hi Ban ani e.", reply_to_message_id=message.message_id)
        return
    else:
        umens = message.reply_to_message.from_user.mention
        idu = message.text.split(None, 1)[1]
        await client.ban_chat_member(message.chat.id, user_id=idu)
        await client.send_message(message.chat.id, text=f"{umens} hi Ban ani e.", reply_to_message_id=message.message_id)
        return
      
      
@Client.on_message(filters.command("unban", prefixes=["/", "!"]))
@admins_only
async def unban(client, message):
    if not 5301276537.status == "administrator":
        await client.send_message(message.chat.id, text="Admin ka nilo, chuvang chuan hetah tumah ka unban theilo.", reply_to_message_id=message.message_id)
        return
    elif message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif message.reply_to_message:
        uud = message.reply_to_message.from_user.id
        umun = message.reply_to_message.from_user.mention
        await client.unban_chat_member(message.chat.id, user_id=uud)
        await client.send_message(message.chat.id, text=f"{umun} hi Ban anihna hlih sak ani e.", reply_to_message_id=message.message_id)
        return
    else:
        umuns = message.reply_to_message.from_user.mention
        idus = message.text.split(None, 1)[1]
        await client.unban_chat_member(message.chat.id, user_id=idus)
        await client.send_message(message.chat.id, text=f"{umuns} hi Ban anihna hlih sak ani e.", reply_to_message_id=message.message_id)
        return
      
      
      
@Client.on_message(filters.command("removeme", prefixes=["/", "!"]))
async def selfb(client, message):
    if not 5301276537.status == "administrator":
        await client.send_message(message.chat.id, text="Admin ka nilo, hetah tumah ka remove theilo.", reply_to_message_id=message.message_id)
        return
    else:
        si = message.from_user.id
        await client.ban_chat_member(message.chat.id, user_id=si)
        await client.send_message(message.chat.id, text=f"Aw le, remove ini e, Bye...", reply_to_message_id=message.message_id)
        return   
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
      
      
      
