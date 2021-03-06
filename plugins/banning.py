# ©️2022 RSR
from pyrogram import Client, filters
from info import GROUPS
from Tereuhte.tetakte.admins import admin_status
from pyrogram.errors import (
    ChatAdminRequired,
    PeerIdInvalid,
    RightForbidden,
    UserNotParticipant,
)



@Client.on_message(filters.command("ban", prefixes=["/", "!"]) & filters.group)
async def ban(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i ban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a ban theih.")
        return
    elif message.reply_to_message:
        try:
            uid = message.reply_to_message.from_user.id
            lal = await message.chat.get_member(uid)
            if lal.status in admin_status:
                return await message.reply_text(
                    "Admin chu ka ban theilo."
                )
            if uid == 1060318977:
                return await message.reply_text(
                    "A ni hi chu min siamtu a ni a, chuvang chuan ka ban ve theilo."
                )
            umen = message.reply_to_message.from_user.mention
            await client.ban_chat_member(message.chat.id, user_id=uid)
            await client.send_message(message.chat.id, text=f"{umen} hi Ban a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka ban theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Ban tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi ban theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Ban tur hi group ah hian a awmlo.")
    else:
        try:
            idu = message.text.split(None, 1)[1]
            lul = await message.chat.get_member(idu)
            if lul.status in admin_status:
                return await message.reply_text(
                    "Admin chu ka ban theilo."
                )
            hmm = await client.get_users(idu)
            if hmm.id == 1060318977:
                return await message.reply_text(
                    "A ni hi chu min siamtu a ni a, chuvang chuan ka ban ve theilo."
                )
            umens = hmm.mention
            await client.ban_chat_member(message.chat.id, user_id=idu)
            await client.send_message(message.chat.id, text=f"{umens} hi Ban a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka ban theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Ban tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi ban theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Ban tur hi group ah hian a awmlo.")
       
    
    
    
@Client.on_message(filters.command("dban", prefixes=["/", "!"]) & filters.group)
async def dban(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i ban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a ban theih.")
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        lal = await message.chat.get_member(uid)
        if lal.status in admin_status:
            return await message.reply_text(
                "Admin chu ka ban theilo."
            )
        if uid == 1060318977:
            return await message.reply_text(
                "A ni hi chu min siamtu a ni a, chuvang chuan ka ban ve theilo."
            )
        umen = message.reply_to_message.from_user.mention
        uii = message.from_user.mention
        await client.ban_chat_member(message.chat.id, user_id=uid)
        await client.send_message(message.chat.id, text=f"{uii} hian {umen} hi a Ban e.")
        await message.reply_to_message.delete()
        await message.delete()
    else:
        idu = message.text.split(None, 1)[1]
        lul = await message.chat.get_member(idu)
        if lul.status in admin_status:
            return await message.reply_text(
                "Admin chu ka ban theilo."
            )
        hmm = await client.get_users(idu)
        if hmm.id == 1060318977:
            return await message.reply_text(
                "A ni hi chu min siamtu a ni a, chuvang chuan ka ban ve theilo."
            )
        umens = hmm.mention
        ull = message.from_user.mention
        await client.ban_chat_member(message.chat.id, user_id=idu)
        await client.send_message(message.chat.id, text=f"{ull} hian {umens} hi a Ban e.")
        await message.delete()    

    return    
    
    
      
      
@Client.on_message(filters.command("unban", prefixes=["/", "!"]) & filters.group)
async def unban(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i unban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a unban theih.")
    elif message.reply_to_message:
        uud = message.reply_to_message.from_user.id
        umun = message.reply_to_message.from_user.mention
        await client.unban_chat_member(message.chat.id, user_id=uud)
        await client.send_message(message.chat.id, text=f"{umun} hi Ban a nihna hlih sak a ni e.", reply_to_message_id=message.id)
    else:
        idus = message.text.split(None, 1)[1]
        haa = await client.get_users(idus)
        umuns = haa.mention
        await client.unban_chat_member(message.chat.id, user_id=idus)
        await client.send_message(message.chat.id, text=f"{umuns} hi Ban a nihna hlih sak a ni e.", reply_to_message_id=message.id)

    return
      
      
      
@Client.on_message(filters.command("removeme", prefixes=["/", "!"]) & filters.group)
async def selfb(client, message):
    si = message.from_user.id
    se = await message.chat.get_member(si)
    if se.status in admin_status:
        return await message.reply_text(
            "Admin i ni a, chuvang chuan ka remove theilo che."
        )
    await client.ban_chat_member(message.chat.id, user_id=si)
    await client.send_message(
        message.chat.id,
        text="Aw le, remove i ni e, Bye...",
        reply_to_message_id=message.id,
    )
    await client.unban_chat_member(message.chat.id, user_id=si)
    
    
    
@Client.on_message(filters.command("remove", prefixes=["/", "!"]) & filters.group)
async def remove(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("Command hmang hian i remove duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a ban theih.")
       return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        lal = await message.chat.get_member(uid)
        if lal.status in admin_status:
            return await message.reply_text(
                "Admin chu ka remove theilo."
            )
        if uid == 1060318977:
            return await message.reply_text(
                "A ni hi chu min siamtu a ni a, chuvang chuan ka remove ve theilo."
            )
        umen = message.reply_to_message.from_user.mention
        await client.ban_chat_member(message.chat.id, user_id=uid)
        await client.send_message(message.chat.id, text=f"{umen} hi remove a ni e.", reply_to_message_id=message.id)
        await client.unban_chat_member(message.chat.id, user_id=uid)
    else:
        idu = message.text.split(None, 1)[1]
        lul = await message.chat.get_member(idu)
        if lul.status in admin_status:
            return await message.reply_text(
                "Admin chu ka remove theilo."
            )
        hmm = await client.get_users(idu)
        if hmm.id == 1060318977:
            return await message.reply_text(
                "A ni hi chu min siamtu a ni a, chuvang chuan ka ban ve theilo."
            )
        umens = hmm.mention
        await client.ban_chat_member(message.chat.id, user_id=idu)
        await client.send_message(message.chat.id, text=f"{umens} hi remove a ni e.", reply_to_message_id=message.id)
        await client.unban_chat_member(message.chat.id, user_id=idu)
    
    
    
    
@Client.on_message(filters.command("mban", prefixes=["/", "!"]) & filters.group)
async def mban(client, message):
    if message.from_user.id != 1060318977:
        await client.send_sticker(message.chat.id, sticker="CAACAgUAAxkBAAI4gmJifVwJRq5boNn1yllknjQaxdXkAAIhAwACjdcwVoyNky4BY4XxJAQ", reply_to_message_id=message.message_id)
        await message.reply_text("Hei chu min siamtu @rsrmusic chauh in a hmang thei aw.")
    elif not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i ban duh message reply in emaw, command zawh ah an ID emaw username dah i thawn chauh in mi a ban theih.")
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await client.ban_chat_member(chat_id=GROUPS, user_id=uid)
        await client.send_message(message.chat.id, text=f"{umen} hi Mass Ban ani e.", reply_to_message_id=message.id)
    else:
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await client.ban_chat_member(chat_id=GROUPS, user_id=idu)
        await client.send_message(message.chat.id, text=f"{umens} hi Mass Ban ani e.", reply_to_message_id=message.id)   

    return   
    
    
      
      
      
