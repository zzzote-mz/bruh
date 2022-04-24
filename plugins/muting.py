# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram.types import ChatPermissions


@Client.on_message(filters.command("mute", prefixes=["/", "!"]) & filters.group)
@admins_only
async def mute(client, message):
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i mute duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a mute theih.**")
       return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=uid, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umen} hi Mute ani e.", reply_to_message_id=message.id)
        return
    else:
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=idu, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umens} hi Mute ani e.", reply_to_message_id=message.id)
        return
 


@Client.on_message(filters.command("dmute", prefixes=["/", "!"]) & filters.group)
@admins_only
async def dmute(client, message):
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i mute duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a mute theih.**")
       return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=uid, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umen} hi Mute ani e.")
        await message.reply_to_message.delete()
        await message.delete()
        return
    else:
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=idu, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umens} hi Mute ani e.")
        await message.reply_to_message.delete()
        await message.delete()
        return



      
@Client.on_message(filters.command("unmute", prefixes=["/", "!"]) & filters.group)
@admins_only
async def unmute(client, message):
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i unmute duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a unmute theih.**")
       return
    elif message.reply_to_message:
        uud = message.reply_to_message.from_user.id
        umun = message.reply_to_message.from_user.mention
        await client.unban_chat_member(chat_id=message.chat.id, user_id=uud)
        await client.send_message(chat_id=message.chat.id, text=f"{umun} hi Mute anihna hlih sak ani e.", reply_to_message_id=message.id)
        return
    else:
        idus = message.text.split(None, 1)[1]
        haa = await client.get_users(idus)
        umuns = haa.mention
        await client.unban_chat_member(chat_id=message.chat.id, user_id=idus)
        await client.send_message(chat_id=message.chat.id, text=f"{umuns} hi Mute anihna hlih sak ani e.", reply_to_message_id=message.id)
        return
      
      
      

    
      
      
      
