import os
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from Tereuhte.tetakte.admins import admin_status
from pyrogram.errors import (
    ChatAdminRequired,
    RightForbidden,
)




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
    try:
        old_title = message.chat.title
        new_title = message.text.split(None, 1)[1]
        await message.chat.set_title(new_title)
        await message.reply_text(
            f"He mi group hming hi **{old_title}** tih aṭangin **{new_title}** tih ah thlak a ni."
        )
        return
    except ChatAdminRequired:
        return await message.reply_text("Admin ka nilo a chuvang chuan group hming ka thlak theilo.")
    except RightForbidden:
        return await message.reply_text("Group hming thlak theihna permission ka neilo.")
  
  
  
  
@Client.on_message(filters.command("setgpic", prefixes=["/", "!"]) & filters.group)
async def setgpic(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
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
        return await message.reply("I thil reply hi a size a lian lutuk.")

    image = await reply.download()
    await message.chat.set_photo(image)
    await message.reply_text("Group icon thlak a ni e.")
    os.remove(image)
    
    
    
    
    
@Client.on_message(filters.command("delgpic", prefixes=["/", "!"]) & filters.group)
async def delgpic(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    try:
        await client.delete_chat_photo(chat_id=message.chat.id)
        await message.reply_text("Group icon delete a ni e.")
        return
    except ChatAdminRequired:
        return await message.reply_text("Admin ka nilo a chuvang chuan group icon ka delete theilo.")
    except RightForbidden:
        return await message.reply_text("Group icon delete theihna permission ka neilo.")
    
    
    
    
    
@Client.on_message(filters.command("report", prefixes=["/", "!"]) | filters.regex("@admin") | filters.regex("@admins") & filters.group)
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
                    gg = message.reply_to_message.from_user.mention
            await message.reply_to_message.reply_text(f"{mention}{gg} message hi Admin hnenah report a ni e.")
    else:
        await message.reply_text("I report duh message reply rawh.")
    
    

    
@Client.on_message(filters.command("setdescription", prefixes=["/", "!"]) & filters.group)
async def setdescription(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if len(message.command) < 2:
        return await message.reply_text("Description tur dah tel rawh.")
    juu = message.text.split(None, 1)[1]
    if len(juu) > 255:
        await message.reply_text("Character 255 aia tam a tih theihloh.")
        return
    try:
        await client.set_chat_description(chat_id=message.chat.id, description=f"{juu}")
        await message.reply_text("Group description siam a ni e.")
        return   
    except ChatAdminRequired:
        return await message.reply_text("Admin ka nilo a chuvang chuan group description ka siam theilo.")
    except RightForbidden:
        return await message.reply_text("Group description siam theihna permission ka neilo.")
    
