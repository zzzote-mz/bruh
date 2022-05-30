# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status
from pyrogram.types import ChatPermissions


@Client.on_message(filters.command("mute", prefixes=["/", "!"]) & filters.group)
async def mute(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i mute duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a mute theih.")
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        lal = await message.chat.get_member(uid)
        if lal.status in admin_status:
            return await message.reply_text(
                "Admin chu ka mute theilo."
            )
        umen = message.reply_to_message.from_user.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=uid, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umen} hi Mute ani e.", reply_to_message_id=message.id)
    else:
        idu = message.text.split(None, 1)[1]
        lul = await message.chat.get_member(idu)
        if lul.status in admin_status:
            return await message.reply_text(
                "Admin chu ka mute theilo."
            )
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=idu, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umens} hi Mute ani e.", reply_to_message_id=message.id)

    return
 


@Client.on_message(filters.command("dmute", prefixes=["/", "!"]) & filters.group)
async def dmute(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i mute duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a mute theih.")
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        lal = await message.chat.get_member(uid)
        if lal.status in admin_status:
            return await message.reply_text(
                "Admin chu ka mute theilo."
            )
        umen = message.reply_to_message.from_user.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=uid, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umen} hi Mute ani e.")
        await message.reply_to_message.delete()
        await message.delete()
    else:
        idu = message.text.split(None, 1)[1]
        lul = await message.chat.get_member(idu)
        if lul.status in admin_status:
            return await message.reply_text(
                "Admin chu ka mute theilo."
            )
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=idu, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text=f"{umens} hi Mute ani e.")
        await message.reply_to_message.delete()
        await message.delete()

    return



      
@Client.on_message(filters.command("unmute", prefixes=["/", "!"]) & filters.group)
async def unmute(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i unmute duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a unmute theih.")
    elif message.reply_to_message:
        uud = message.reply_to_message.from_user.id
        umun = message.reply_to_message.from_user.mention
        await client.unban_chat_member(chat_id=message.chat.id, user_id=uud)
        await client.send_message(chat_id=message.chat.id, text=f"{umun} hi Mute anihna hlih sak ani e.", reply_to_message_id=message.id)
    else:
        idus = message.text.split(None, 1)[1]
        haa = await client.get_users(idus)
        umuns = haa.mention
        await client.unban_chat_member(chat_id=message.chat.id, user_id=idus)
        await client.send_message(chat_id=message.chat.id, text=f"{umuns} hi Mute anihna hlih sak ani e.", reply_to_message_id=message.id)

    return
      
      
      

    
      
      
      
