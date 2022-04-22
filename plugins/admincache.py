from pyrogram import Client, filters
from Tereuhte.tetakte.cahce import ADMIN_CACHE, TEMP_ADMIN_CACHE_BLOCK, admin_cache_reload










async def adminlist_show(_, m: Message):
    global ADMIN_CACHE
    if m.chat.type != "supergroup":
        return await m.reply_text(
            "This command is made to be used in groups only!",
        )
    try:
        try:
            admin_list = ADMIN_CACHE[m.chat.id]
            note = tlang(m, "admin.adminlist.note_cached")
        except KeyError:
            admin_list = await admin_cache_reload(m, "adminlist")
            note = tlang(m, "admin.adminlist.note_updated")

        adminstr = (tlang(m, "admin.adminlist.adminstr")).format(
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

        adminstr += "<b>User Admins:</b>\n"
        adminstr += "\n".join(f"- {i}" for i in mention_users)
        adminstr += "\n\n<b>Bots:</b>\n"
        adminstr += "\n".join(f"- {i}" for i in mention_bots)

        await m.reply_text(adminstr + "\n\n" + note)
        LOGGER.info(f"Adminlist cmd use in {m.chat.id} by {m.from_user.id}")

    except Exception as ef:
        if str(ef) == str(m.chat.id):
            await m.reply_text(tlang(m, "admin.adminlist.use_admin_cache"))
        else:
            ef = str(ef) + f"{admin_list}\n"
            await m.reply_text(
                (tlang(m, "general.some_error")).format(
                    SUPPORT_GROUP=SUPPORT_GROUP,
                    ef=ef,
                ),
            )
        LOGGER.error(ef)
        LOGGER.error(format_exc())

    return
