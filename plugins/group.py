import os
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram.enums import ChatMembersFilter
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
    
    
    
    
    
@Client.on_message(filters.command("report") | filters.regex("@admin") | filters.regex("@admins") & filters.group)
async def report_user(client, message):
    if message.reply_to_message:
        check_admin = await message.chat.get_member(message.reply_to_message.from_user.id)
        if check_admin.status not in admin_status:
            mention = ""
            async for i in message.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
                if not (
                    i.user.is_deleted or i.privileges.is_anonymous or i.user.is_bot
                ):
                    mention += f"<a href='tg://user?id={i.user.id}'>\u2063</a>"
            await message.reply_to_message.reply_text(
                    "{}{} message hi Admin hnenah report a ni e.").format(
                    mention,
                    message.reply_to_message.from_user.mention(),
            )
    else:
        await message.reply_text("I report duh message reply rawh.")
    
    

    
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
    
    
    
