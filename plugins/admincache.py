from pyrogram import Client, filters
from Tereuhte.tetakte.cache import ADMIN_CACHE, admin_cache_reload
from Tereuhte.tetakte.parse import mention_html, mention_markdown
from Tereuhte.tetakte.helper import admins_only







@Client.on_message(filters.command("admins", prefixes=["/", "!"]))
async def adminlist(client, message):
    global ADMIN_CACHE
    if message.chat.type == "private":
        return await message.reply_text(
            "**Hei chu group ah chauh a hman theih.**",
        )
    try:
       admin_list = ADMIN_CACHE[message.chat.id]
    except KeyError:
       admin_list = await admin_cache_reload(message, "adminlist")
    adminstr = (f"**{message.chat.title}** a Admin te chu." + "\n\n")

    bot_admins = [i for i in admin_list if (i[1].lower()).endswith("bot")]
    user_admins = [i for i in admin_list if not (i[1].lower()).endswith("bot")]

    mention_users = [
        (
            admin[1]
            if admin[1].startswith("@")
            else (await mention_markdown(admin[1], admin[0]))
        )
        for admin in user_admins
        if not admin[2]  
    ]
    mention_users.sort(key=lambda x: x[1])

    mention_bots = [
        (
            admin[1]
            if admin[1].startswith("@")
            else (await mention_markdown(admin[1], admin[0]))
        )
        for admin in bot_admins
    ]
    mention_bots.sort(key=lambda x: x[1])

    adminstr += "<b><u>User Admin te:</b></u>\n"
    adminstr += "\n".join(f"➥ {i}" for i in mention_users)
    adminstr += "\n\n<b><u>Bot:</b></u>\n"
    adminstr += "\n".join(f"➥ {i}" for i in mention_bots)

    await message.reply_text(adminstr)


    
@Client.on_message(filters.command("admincache", prefixes=["/", "!"]) & filters.group)    
@admins_only
async def reload_admins(client, message):
    await admin_cache_reload(message, "admincache")
    await message.reply_text("**Admin list refresh ani e ✅**")
        
    
    
    
