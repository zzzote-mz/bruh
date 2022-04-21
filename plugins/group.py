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
  
  
  
  
@Client.on_message(filters.command("setgtitle", prefixes=["/", "!"]))
@admins_only
