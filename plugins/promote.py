# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram.types import ChatPrivileges


@Client.on_message(filters.command("fpromote", prefixes=["/", "!"]) & filters.group)
@admins_only
async def fpromote(client, message):
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("**Command hmang hian i promote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a promote theih.**")
    elif message.reply_to_message:
        bot = await client.get_chat_member(chat_id=message.chat.id, user_id=5395576724)
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
        await client.send_message(message.chat.id, text=f"{umen} hi Promote ani e.", reply_to_message_id=message.id)
    else:
        bot = await client.get_chat_member(chat_id=message.chat.id, user_id=5395576724)
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
        await client.send_message(message.chat.id, text=f"{umens} hi Promote ani e.", reply_to_message_id=message.id)

    return
    
@Client.on_message(filters.command("lpromote", prefixes=["/", "!"]) & filters.group)
@admins_only
async def lpromote(client, message):
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("**Command hmang hian i promote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a promote theih.**")
    elif message.reply_to_message:
        bot = await client.get_chat_member(chat_id=message.chat.id, user_id=5395576724)
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
        await client.send_message(message.chat.id, text=f"{umen} hi Promote ani e.", reply_to_message_id=message.id)
    else:
        bot = await client.get_chat_member(chat_id=message.chat.id, user_id=5395576724)
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await member.chat.promote_member(
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
        await client.send_message(message.chat.id, text=f"{umens} hi Promote ani e.", reply_to_message_id=message.id)   

    return   
    
    
      
      
@Client.on_message(filters.command("demote", prefixes=["/", "!"]) & filters.group)
@admins_only
async def demote(client, message):
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("**Command hmang hian i demote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a demote theih.**")
    elif message.reply_to_message:
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
        await client.send_message(message.chat.id, text=f"{umun} hi Admin anihna hlih sak ani e.", reply_to_message_id=message.id)
    else:
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
        await client.send_message(message.chat.id, text=f"{umuns} hi Admin anihna hlih sak ani e.", reply_to_message_id=message.id)

    return
      
      
      

@Client.on_message(filters.command("title", prefixes=["/", "!"]) & filters.group)
@admins_only
async def title(client, message):
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
    title = message.text.split(None, 1)[1]
    await client.set_administrator_title(chat_id, from_user.id, title)
    await message.reply_text(
        f"{from_user.mention} hi a Admin title **{title}** tia siam sak ani."
    )
      
      
      
