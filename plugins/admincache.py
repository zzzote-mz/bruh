from pyrogram import Client, filters
from Tereuhte.tetakte.cache import ADMIN_CACHE, TEMP_ADMIN_CACHE_BLOCK, admin_cache_reload
from Tereuhte.tetakte.parse import mention_html
from Tereuhte.tetakte.helper import admins_only
from info import ADMINS






@Client.on_message(filters.command("admins", prefixes=["/", "!"]))
async def adminlist(client, message):
    global ADMIN_CACHE
    if message.chat.type == "private":
        return await message.reply_text(
            "**Hei chu group ah chauh a hman theih.**",
        )
    try:
        admin_list = ADMIN_CACHE[message.chat.id]
        note = "Cache value."
    except KeyError:
        admin_list = await admin_cache_reload(message, "adminlist")
        note = "Up to date value."

    adminstr = "**{}** a Admin te chu.".format(
        message.chat.title,
    ) + "\n\n"

    bot_admins = [i for i in admin_list if (i[1].lower()).endswith("bot")]
    user_admins = [i for i in admin_list if not (i[1].lower()).endswith("bot")]

    # format is like: (user_id, username/name,anonyamous or not)
    mention_users = [
        (
            admin[1]
            if admin[1].startswith("@")
            else (await mention_html(admin[1], admin[0]))
        )
        for admin in user_admins
        if not admin[2]  # if non-anonyamous admin
    ]
    mention_users.sort(key=lambda x: x[1])

    mention_bots = [
        (
            admin[1]
            if admin[1].startswith("@")
            else (await mention_html(admin[1], admin[0]))
        )
        for admin in bot_admins
    ]
    mention_bots.sort(key=lambda x: x[1])

    adminstr += "<b><u>User Admin te:</b></u>\n"
    adminstr += "\n".join(f"- {i}" for i in mention_users)
    adminstr += "\n\n<b><u>Bot:</b></u>\n"
    adminstr += "\n".join(f"- {i}" for i in mention_bots)

    await message.reply_text(adminstr + "\n\n" + note)


    
@Client.on_message(filters.command("admincache", prefixes=["/", "!"]) & filters.group)    
@admins_only
async def reload_admins(client, message):
    global TEMP_ADMIN_CACHE_BLOCK

    if (
        (message.chat.id in set(TEMP_ADMIN_CACHE_BLOCK.keys()))
        and (message.from_user.id not in ADMINS)
        and TEMP_ADMIN_CACHE_BLOCK[message.chat.id] == "manualblock"
    ):
        await message.reply_text("Minute 10 dan ah chiah admin list a refresh theih.")
        return
       
        await admin_cache_reload(message, "admincache")
        TEMP_ADMIN_CACHE_BLOCK[message.chat.id] = "manualblock"
        await message.reply_text("**Admin list refresh ani e ✅**")
        
    
    
    
