from pyrogram import Client, filters
from pyrogram.types import CallbackQuery




@Client.on_callback_query(filters.regex("^close_admin$"))
async def close_admin_callback(client, query):
    user_id = query.from_user.id
    user_status = (await query.message.chat.get_member(user_id)).status
    if user_status not in {"creator", "administrator"}:
        await query.answer(
            "Group creator chiah in a ti thei.",
            show_alert=True,
        )
        return
    if user_status != "creator":
        await query.answer(
            "Group creator chiah in a ti thei.",
            show_alert=True,
        )
        return
    await query.message.edit_text("Sût leh ani e.")
    await query.answer()
    return




@Client.on_callback_query(filters.regex("^close_i$"))
async def close_admin(client, query):
    user_id = query.from_user.id
    user_mention = query.from_user.mention
    user_status = (await query.message.chat.get_member(user_id)).status
    if user_status not in {"creator", "administrator"}:
        await query.answer(
            "Group Admin inih loh chuan iti ve theilo.",
            show_alert=True,
        )
        return
    await query.message.edit_text(f"{user_mention} hian warning a remove e.")
    await query.answer()
    return




@Client.on_callback_query(filters.regex("^web_app$"))
async def close_admin(client, query):
    answer_web_app_query("https://www.imrsr.online")
    return




