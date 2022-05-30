from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from Tereuhte.tetakte.owner import owner_status
from Tereuhte.tetakte.admins import admin_status


@Client.on_callback_query(filters.regex("^close_admin$"))
async def close_admin_callback(client, query):
    user_id = query.from_user.id
    user_status = (await query.message.chat.get_member(user_id)).status
    if not user_status in owner_status:
        await query.answer(
            "Group creator chiah in a ti thei",
            show_alert=True,
        )
        return
    if user_status in owner_status and user_id == 1060318977:
        await query.message.edit_text("Sût leh a ni e.")
        await query.answer()
        return




@Client.on_callback_query(filters.regex("^close_i$"))
async def close_admin(client, query):
    user_id = query.from_user.id
    user_mention = query.from_user.mention
    user_status = (await query.message.chat.get_member(user_id)).status
    if not user_status in admin_status:
        await query.answer(
            "Admin i nih loh chuan i ti ve theilo",
            show_alert=True,
        )
        return
    if user_status in admin_status and user_id == 1060318977:
        await query.message.edit_text(f"{user_mention} hian warning a remove e.")
        await query.answer()
        return









