from pyrogram import Client, filters
from Tereuhte.tetakte.cahce import ADMIN_CACHE, TEMP_ADMIN_CACHE_BLOCK, admin_cache_reload









@Client.on_message(filters.command("admins", prefixes=["/", "!"]) & filters.group)
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

    adminstr = f"**{chat_title}** a Admin te chu:".format(
        chat_title=m.chat.title,
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

    adminstr += "<b>User Admin te:</b>\n"
    adminstr += "\n".join(f"- {i}" for i in mention_users)
    adminstr += "\n\n<b>Bot:</b>\n"
    adminstr += "\n".join(f"- {i}" for i in mention_bots)

    await m.reply_text(adminstr + "\n\n" + note)

return
