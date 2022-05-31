# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status
from pyrogram.types import ChatPrivileges
from pyrogram.errors import (
    ChatAdminRequired,
    PeerIdInvalid,
    RightForbidden,
    UserNotParticipant,
)



@Client.on_message(filters.command("fpromote", prefixes=["/", "!"]) & filters.group)
async def fpromote(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("**Command hmang hian i promote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a promote theih.**")
    elif message.reply_to_message:
        try:
            uid = message.reply_to_message.from_user.id
            umen = message.reply_to_message.from_user.mention
            await message.chat.promote_member(
                user_id=uid,
                privileges=ChatPrivileges(
                    can_change_info=True,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ),
            )
            await client.send_message(message.chat.id, text=f"{umen} hi Promote a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka promote theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Promote tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi promote theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Promote tur hi group ah hian a awmlo.")
    else:
        try:
            idu = message.text.split(None, 1)[1]
            hmm = await client.get_users(idu)
            umens = hmm.mention
            await message.chat.promote_member(
                user_id=idu,
                privileges=ChatPrivileges(
                    can_change_info=True,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ),
            )
            await client.send_message(message.chat.id, text=f"{umens} hi Promote a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka promote theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Promote tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi promote theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Promote tur hi group ah hian a awmlo.")
    
    
@Client.on_message(filters.command("lpromote", prefixes=["/", "!"]) & filters.group)
async def lpromote(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("**Command hmang hian i promote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a promote theih.**")
    elif message.reply_to_message:
        try:
            uid = message.reply_to_message.from_user.id
            umen = message.reply_to_message.from_user.mention
            await message.chat.promote_member(
                user_id=uid,
                privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ),
            )
            await client.send_message(message.chat.id, text=f"{umen} hi Promote a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka promote theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Promote tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi promote theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Promote tur hi group ah hian a awmlo.")
    else:
        try:
            idu = message.text.split(None, 1)[1]
            hmm = await client.get_users(idu)
            umens = hmm.mention
            await message.chat.promote_member(
                user_id=idu,
                privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ),
            )
            await client.send_message(message.chat.id, text=f"{umens} hi Promote a ni e.", reply_to_message_id=message.id)   
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka promote theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Promote tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi promote theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Promote tur hi group ah hian a awmlo.")
    
    
    
      
      
@Client.on_message(filters.command("demote", prefixes=["/", "!"]) & filters.group)
async def demote(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("**Command hmang hian i demote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a demote theih.**")
    elif message.reply_to_message:
        try:
            uud = message.reply_to_message.from_user.id
            umun = message.reply_to_message.from_user.mention
            await message.chat.promote_member(
                user_id=uud,
                privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                ),
            )
            await client.send_message(message.chat.id, text=f"{umun} hi Admin anihna hlih sak a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka demote theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Demote tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi demote theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Demote tur hi group ah hian a awmlo.")
    else:
        try:
            idus = message.text.split(None, 1)[1]
            haa = await client.get_users(idus)
            umuns = haa.mention
            await message.chat.promote_member(
                user_id=idus,
                privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                ),
            )
            await client.send_message(message.chat.id, text=f"{umuns} hi Admin anihna hlih sak a ni e.", reply_to_message_id=message.id)
        except ChatAdminRequired:
            return await message.reply_text("Admin ka nilo a chuvang chuan tumah ka demote theilo.")
        except PeerIdInvalid:
            return await message.reply_text("Demote tur ID hi ka hmulo.")
        except RightForbidden:
            return await message.reply_text("Hetah mi demote theihna permission ka neilo.")
        except UserNotParticipant:
            return await message.reply_text("Demote tur hi group ah hian a awmlo.")
    
      
      
      

@Client.on_message(filters.command("title", prefixes=["/", "!"]) & filters.group)
async def title(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if not message.reply_to_message:
        return await message.reply_text(
            "Command hmang hian title i siam sak duh message reply la, command zawh ah a title tur dah rawh."
        )
    if not message.reply_to_message.from_user:
        return await message.reply_text(
            "I message reply hi title ka siam sak theilo."
        )
    chat_id = message.chat.id
    from_user = message.reply_to_message.from_user
    if len(message.command) < 2:
        return await message.reply_text(
            "A title tur dah tel rawh."
        )
    try:
        title = message.text.split(None, 1)[1]
        await client.set_administrator_title(chat_id, from_user.id, title)
        await message.reply_text(
            f"{from_user.mention} hi a Admin title **{title}** ti a siam sak a ni."
        )
    except ChatAdminRequired:
        return await message.reply_text("Admin ka nilo a chuvang chuan tumah Admin title ka siam sak theilo.")
    except PeerIdInvalid:
        return await message.reply_text("Admin title siam sak tur ID hi ka hmulo.")
    except RightForbidden:
        return await message.reply_text("Hetah mi Admin title siam sak theihna permission ka neilo.")
    except UserNotParticipant:
        return await message.reply_text("Admin title siam sak tur hi group ah hian a awmlo.")
      
      
   


@Client.on_message(filters.command("promoteme", prefixes=["/", "!"]) & filters.group)
async def fpromote(client, message):
    heh = message.from_user.id
    if not heh == 1060318977:
        return await message.reply_text(
            "Hei chu min siamtu chauh in a hmang thei."
        )
    await message.chat.promote_member(
        user_id=1060318977,
        privileges=ChatPrivileges(
            can_change_info=True,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_chat=True,
            can_manage_video_chats=True,
        ),
    )
    await client.send_message(message.chat.id, text="Done Master 😊", reply_to_message_id=message.id)
    return





@Client.on_message(filters.command("demoteme", prefixes=["/", "!"]) & filters.group)
async def demote(client, message):
    heh = message.from_user.id
    if not heh == 1060318977:
        return await message.reply_text(
            "Hei chu min siamtu chauh in a hmang thei."
        )
    await message.chat.promote_member(
        user_id=1060318977,
        privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False,
        ),
    )
    await client.send_message(message.chat.id, text="Done Master 😊", reply_to_message_id=message.id)
    return
    


