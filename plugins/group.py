import os
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram import enums
from Tereuhte.tetakte.admins import admin_status


@Client.on_message(filters.command("setgtitle", prefixes=["/", "!"]) & filters.group)
async def setgtitle(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if len(message.command) < 2:
        return await message.reply_text("A hming tur dah tel rawh.")
    old_title = message.chat.title
    new_title = message.text.split(None, 1)[1]
    await message.chat.set_title(new_title)
    await message.reply_text(
        f"He mi group hming hi **{old_title}** tih aṭangin **{new_title}** tih ah thlak ani."
    )
    return
  
  
  
  
@Client.on_message(filters.command("setgpic", prefixes=["/", "!"]) & filters.group)
@admins_only
async def setgpic(client, message):
    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "Thlalak emaw thlalak document file reply rawh."
        )

    file = reply.document or reply.photo
    if not file:
        return await message.reply_text(
            "Thlalak emaw thlalak document file reply rawh."
        )

    if file.file_size > 5000000:
        return await message.reply("I thil reply hi a size a lian lutuk, ka ti theilo..")

    photo = await reply.download()
    await message.chat.set_photo(photo)
    await message.reply_text("Group icon thlak ani e.")
    os.remove(photo)
    
    
    
    
    
@Client.on_message(filters.command("delgpic", prefixes=["/", "!"]) & filters.group)
@admins_only   
async def delgpic(client, message):
    await client.delete_chat_photo(chat_id=message.chat.id)
    await message.reply_text("Group icon delete ani e.")
    return
    
    
    
    
    
@Client.on_message(filters.command(["admin", "admins", "report"], prefixes="@") & filters.group)
async def report_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "I report duh message reply rawh."
        )

    reply = message.reply_to_message
    reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    user_id = message.from_user.id if message.from_user else message.sender_chat.id
    linked_chat = (await client.get_chat(message.chat.id)).linked_chat
    if linked_chat is not None:
        heh = message.reply_to_message.from_user.id
        huh = await message.chat.get_member(heh)
        if huh.status in admin_status or reply_id == message.chat.id or reply_id == linked_chat.id:
            return await message.reply_text(
                "Admin i report theilo."
            )
    else:
        hih = message.reply_to_message.from_user.id
        hah = await message.chat.get_member(hih)
        if hah.status in admin_status or reply_id == message.chat.id:
            return await message.reply_text(
                "Admin i report theilo."
            )
        user_mention = message.reply_to_message.from_user.mention
        text = f"{user_mention} message hi Admin hnen ah report ani e."
        admin = list(await client.get_chat_members(
            chat_id=message.chat.id,
            filter=enums.ChatMembersFilter.ADMINISTRATORS))
        if not (admin.user.is_deleted or admin.is_anonymous or admin.user.is_bot):
            text += f"[\u2063](tg://user?id={admin.user.id})"

        await message.reply_to_message.reply_text(text)  
    
    

    
@Client.on_message(filters.command("setdescription", prefixes=["/", "!"]) & filters.group)
@admins_only   
async def setdescription(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Description tur dah tel rawh.")
    juu = message.text.split(None, 1)[1]
    if len(juu) > 255:
        await message.reply_text("Character 255 aia tam a tih theihloh.")
        return
    await client.set_chat_description(chat_id=message.chat.id, description=f"{juu}")
    await message.reply_text("Group description siam ani e.")
    return   
    
    
    
