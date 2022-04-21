import os
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("setgtitle", prefixes=["/", "!"]))
@admins_only
async def setgtitle(client, message):
    if len(message.command) < 2:
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
    await client.delete_chat_photo(chat_id=message.chat.id)
    await message.reply_text("Group icon delete ani e.")
    
    
    
    
    
