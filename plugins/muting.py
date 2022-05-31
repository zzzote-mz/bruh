# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status
from pyrogram.types import ChatPermissions
from pyrogram.errors import (
    ChatAdminRequired,
    PeerIdInvalid,
    RightForbidden,
    UserNotParticipant,
)




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
        try:
            uid = message.reply_to_message.from_user.id
            lal = await message.chat.get_member(uid)
            if lal.status in admin_status:
                return await message.reply_text(
                    "Admin chu ka mute theilo."
                )
            if uid == 1060318977:
                return await message.reply_text(
                    "A ni hi chu min siamtu a ni a, chuvang chuan ka mute ve theilo."
                )
            umen = message.reply_to_message.from_user.mention
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=uid, permissions=ChatPermissions())
            await client.send_message(message.chat.id, text=f"{umen} hi Mute a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka mute theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Mute tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi mute theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Mute tur hi group ah hian a awmlo.")
    else:
        try:
            idu = message.text.split(None, 1)[1]
            lul = await message.chat.get_member(idu)
            if lul.status in admin_status:
                return await message.reply_text(
                    "Admin chu ka mute theilo."
                )
            hmm = await client.get_users(idu)
            if hmm.id == 1060318977:
                return await message.reply_text(
                    "A ni hi chu min siamtu a ni a, chuvang chuan ka mute ve theilo."
                )
            umens = hmm.mention
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=idu, permissions=ChatPermissions())
            await client.send_message(message.chat.id, text=f"{umens} hi Mute a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka mute theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Mute tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi mute theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Mute tur hi group ah hian a awmlo.")
        
 


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
        try:
            uid = message.reply_to_message.from_user.id
            lal = await message.chat.get_member(uid)
            if lal.status in admin_status:
                return await message.reply_text(
                    "Admin chu ka mute theilo."
                )
            if uid == 1060318977:
                return await message.reply_text(
                    "A ni hi chu min siamtu a ni a, chuvang chuan ka mute ve theilo."
                )
            umen = message.reply_to_message.from_user.mention
            ull = message.from_user.mention
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=uid, permissions=ChatPermissions())
            await client.send_message(message.chat.id, text=f"{ull} hian {umen} hi a Mute e.")
            await message.reply_to_message.delete()
            await message.delete()
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka mute theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Mute tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi mute theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Mute tur hi group ah hian a awmlo.")
    else:
        try:
            idu = message.text.split(None, 1)[1]
            lul = await message.chat.get_member(idu)
            if lul.status in admin_status:
                return await message.reply_text(
                    "Admin chu ka mute theilo."
                )
            hmm = await client.get_users(idu)
            if hmm.id == 1060318977:
                return await message.reply_text(
                    "A ni hi chu min siamtu a ni a, chuvang chuan ka mute ve theilo."
                )
            umens = hmm.mention
            uii = message.from_user.mention
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=idu, permissions=ChatPermissions())
            await client.send_message(message.chat.id, text=f"{uii} hian {umens} hi a Mute e.")
            await message.delete()
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka mute theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Mute tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi mute theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Mute tur hi group ah hian a awmlo.")
    



      
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
        try:
            uud = message.reply_to_message.from_user.id
            umun = message.reply_to_message.from_user.mention
            await client.unban_chat_member(chat_id=message.chat.id, user_id=uud)
            await client.send_message(chat_id=message.chat.id, text=f"{umun} hi Mute anihna hlih sak a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka unmute theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Unmute tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi unmute theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Unmute tur hi group ah hian a awmlo.")
    else:
        try:
            idus = message.text.split(None, 1)[1]
            haa = await client.get_users(idus)
            umuns = haa.mention
            await client.unban_chat_member(chat_id=message.chat.id, user_id=idus)
            await client.send_message(chat_id=message.chat.id, text=f"{umuns} hi Mute anihna hlih sak a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka unmute theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Unmute tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi unmute theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Unmute tur hi group ah hian a awmlo.")
    
      
      
      

    
      
      
      
