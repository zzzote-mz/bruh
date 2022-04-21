import os
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only



admins_in_chat = {}

async def list_admins(chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in app.iter_chat_members(
                chat_id, filter="administrators"
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]



@Client.on_message(filters.command("setgtitle", prefixes=["/", "!"]))
@admins_only
async def setgtitle(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif len(message.command) < 2:
        return await message.reply_text("A hming tur dah tel rawh.")
    old_title = message.chat.title
    new_title = message.text.split(None, 1)[1]
    await message.chat.set_title(new_title)
    await message.reply_text(
        f"He mi group hming hi **{old_title}** tih aṭangin **{new_title}** tih ah thlak ani."
    )
    return
  
  
  
  
@Client.on_message(filters.command("setgpic", prefixes=["/", "!"]))
@admins_only
async def setgpic(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
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
    
    
    
    
    
@Client.on_message(filters.command("delgpic", prefixes=["/", "!"]))
@admins_only   
async def delgpic(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
            await client.delete_chat_photo(chat_id=message.chat.id)
            await message.reply_text("Group icon delete ani e.")
            return
    
    
    
    
    
@Client.on_message(filters.command(["admin", "admins", "report"], prefixes="@"))
@admins_only
async def report_user(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    if not message.reply_to_message:
        return await message.reply_text(
            "I report duh message reply rawh."
        )

    reply = message.reply_to_message
    reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    user_id = message.from_user.id if message.from_user else message.sender_chat.id
    list_of_admins = await list_admins(message.chat.id)
    linked_chat = (await client.get_chat(message.chat.id)).linked_chat
    if linked_chat is not None:
        if reply_id in list_of_admins or reply_id == message.chat.id or reply_id == linked_chat.id:
            return await message.reply_text(
                "Admin i report theilo."
            )
    else:
        if reply_id in list_of_admins or reply_id == message.chat.id:
            return await message.reply_text(
                "Admin i report theilo."
            )

    user_mention = reply.from_user.mention if reply.from_user else reply.sender_chat.title
    text = f"{user_mention} message hi Admin hnen ah report ani."
    admin_data = await client.get_chat_members(
        chat_id=message.chat.id, filter="administrators"
    ) 
    for admin in admin_data:
        if admin.user.is_bot or admin.user.is_deleted:
            continue
        text += f"[\u2063](tg://user?id={admin.user.id})"

    await message.reply_to_message.reply_text(text)    
    
    
