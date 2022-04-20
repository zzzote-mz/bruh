# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only



@Client.on_message(filters.command("fpromote", prefixes=["/", "!"]))
@admins_only
async def fpromote(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i promote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a promote theih.**")
       return
    elif message.reply_to_message:
        bot = await client.get_chat_member(message.chat.id, 5301276537)
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await message.chat.promote_member(
            user_id=uid,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=bot.can_restrict_members,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await client.send_message(message.chat.id, text=f"{umen} hi Promote ani e.", reply_to_message_id=message.message_id)
        return
    else:
        bot = await client.get_chat_member(message.chat.id, 5301276537)
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await member.chat.promote_member(
            user_id=idu,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=bot.can_restrict_members,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await client.send_message(message.chat.id, text=f"{umens} hi Promote ani e.", reply_to_message_id=message.message_id)
        return
    
@Client.on_message(filters.command("lpromote", prefixes=["/", "!"]))
@admins_only
async def lpromote(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i promote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a promote theih.**")
       return
    elif message.reply_to_message:
        bot = await client.get_chat_member(message.chat.id, 5301276537)
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await message.chat.promote_member(
            user_id=uid,
            can_change_info=False,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await client.send_message(message.chat.id, text=f"{umen} hi Promote ani e.", reply_to_message_id=message.message_id)
        return
    else:
        bot = await client.get_chat_member(message.chat.id, 5301276537)
        idu = message.text.split(None, 1)[1]
        hmm = await client.get_users(idu)
        umens = hmm.mention
        await member.chat.promote_member(
            user_id=idu,
            can_change_info=False,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await client.send_message(message.chat.id, text=f"{umens} hi Promote ani e.", reply_to_message_id=message.message_id)
        return   
    
    
      
      
@Client.on_message(filters.command("demote", prefixes=["/", "!"]))
@admins_only
async def demote(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i demote duh message reply in emaw, command zawh ah an ID emaw username dah a i thawn chauh in mi a demote theih.**")
       return
    elif message.reply_to_message:
        uud = message.reply_to_message.from_user.id
        umun = message.reply_to_message.from_user.mention
        await message.chat.promote_member(
            user_id=uud,
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_voice_chats=False,
        )
        await client.send_message(message.chat.id, text=f"{umun} hi Admin anihna hlih sak ani e.", reply_to_message_id=message.message_id)
        return
    else:
        idus = message.text.split(None, 1)[1]
        haa = await client.get_users(idus)
        umuns = haa.mention
        await message.chat.promote_member(
            user_id=idus,
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_voice_chats=False,
        )
        await client.send_message(message.chat.id, text=f"{umuns} hi Admin anihna hlih sak ani e.", reply_to_message_id=message.message_id)
        return
      
      
      

    
      
      
      
