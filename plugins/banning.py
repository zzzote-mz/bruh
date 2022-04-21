# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("ban", prefixes=["/", "!"]))
@admins_only
async def ban(client, message):
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i ban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a ban theih.**")
       return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.ban_chat_member(message.chat.id, user_id=uid)
        await client.send_message(message.chat.id, text=f"{umen} hi Ban ani e.", reply_to_message_id=message.message_id)
        return
    else:
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.ban_chat_member(message.chat.id, user_id=idu)
        await client.send_message(message.chat.id, text=f"{umens} hi Ban ani e.", reply_to_message_id=message.message_id)
        return
      
      
@Client.on_message(filters.command("unban", prefixes=["/", "!"]))
@admins_only
async def unban(client, message):
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i unban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a unban theih.**")
       return
    elif message.reply_to_message:
        uud = message.reply_to_message.from_user.id
        umun = message.reply_to_message.from_user.mention
        await client.unban_chat_member(message.chat.id, user_id=uud)
        await client.send_message(message.chat.id, text=f"{umun} hi Ban anihna hlih sak ani e.", reply_to_message_id=message.message_id)
        return
    else:
        idus = message.text.split(None, 1)[1]
        haa = await client.get_users(idus)
        umuns = haa.mention
        await client.unban_chat_member(message.chat.id, user_id=idus)
        await client.send_message(message.chat.id, text=f"{umuns} hi Ban anihna hlih sak ani e.", reply_to_message_id=message.message_id)
        return
      
      
      
@Client.on_message(filters.command("removeme", prefixes=["/", "!"]))
async def selfb(client, message):
    si = message.from_user.id
    await client.ban_chat_member(message.chat.id, user_id=si)
    await client.send_message(message.chat.id, text=f"Aw le, remove ini e, Bye...", reply_to_message_id=message.message_id)
    await asyncio.sleep(1)
    await client.unban_chat_member(message.chat.id, user_id=si)
    
    
    
@Client.on_message(filters.command("remove", prefixes=["/", "!"]))
@admins_only
async def remove(client, message):
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i ban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a ban theih.**")
       return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.ban_chat_member(message.chat.id, user_id=uid)
        await client.send_message(message.chat.id, text=f"{umen} hi Ban ani e.", reply_to_message_id=message.message_id)
        await asyncio.sleep(1)
        await client.unban_chat_member(message.chat.id, user_id=uid)
    else:
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.ban_chat_member(message.chat.id, user_id=idu)
        await client.send_message(message.chat.id, text=f"{umens} hi Ban ani e.", reply_to_message_id=message.message_id)
        await asyncio.sleep(1)
        await client.unban_chat_member(message.chat.id, user_id=idu)
    
    
    
    
    
      
      
      
