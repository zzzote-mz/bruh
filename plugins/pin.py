# ©️2022 RSR
from pyrogram.errors import RightForbidden, MessageIdInvalid
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status
from Tereuhte.tetakte.owner import owner_status
from pyrogram.filters import regex
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("pin", prefixes=["/", "!"]) & filters.group)
async def pin_message(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    pin_args = message.text.split(None, 1)
    if message.reply_to_message:
        try:
            disable_notification = len(pin_args) < 2 or pin_args[1] not in ["loud"]
            await message.reply_to_message.pin(
                disable_notification=disable_notification,
            )

            if message.chat.username:
                link_chat_id = message.chat.username
                hmm = (
                    f"https://t.me/{link_chat_id}/{message.reply_to_message.id}"
                )
            elif (str(message.chat.id)).startswith("-100"):
                link_chat_id = (str(message.chat.id)).replace("-100", "")
                hmm = (
                    f"https://t.me/c/{link_chat_id}/{message.reply_to_message.id}"
                )
            rsrke = InlineKeyboardMarkup(
                        [
                           [
                               InlineKeyboardButton(
                                   "Message pin en na", url=f"{hmm}"
                               ),
                           ],
                       ]
                    )
            await message.reply_text(
                "**He message hi ka pin e.**",
                reply_markup=rsrke
            )

        except RightForbidden:
            await message.reply_text("He mi group ah hian message pin theihna permission ka neilo.")
    else:
        await message.reply_text("**I pin tur message reply rawh.**")

    return







@Client.on_message(filters.command("unpin", prefixes=["/", "!"]) & filters.group)
async def unpin_message(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    try:
        if message.reply_to_message:
            await client.unpin_chat_message(message.chat.id, message.reply_to_message.id)
            await message.reply_text("**Message unpin a ni e.**")
        else:
            await client.unpin_chat_message(message.chat.id)
            await message.reply_text("**Message pin hnu hnun ber unpin a ni e.**")
    except RightForbidden:
        await message.reply_text("**Hetah message pin emaw unpin theihna permission ka neilo.**")
    except MessageIdInvalid:
        await message.reply_text("**Message unpin tur ID hi ka hmu theilo.**")
    
    return
                                     
                                     
                                     
@Client.on_message(filters.command("unpinall", prefixes=["/", "!"]) & filters.group)
async def unpinall_message(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in owner_status:
        return await message.reply_text(
            "Group creator chauh in a ti thei."
        )
    rsrkey = InlineKeyboardMarkup(
                 [
                     [
                         InlineKeyboardButton(
                             "Aw", callback_data="unpin_all_in_this_chat"
                         ),
                         InlineKeyboardButton(
                             "Aih", callback_data="close_admin"
                         ),
                     ],
                 ]
             )
    await message.reply_text(
        "**Group a message pin zawng zawng hi unpin vek i duh tih i chiang maw?**",
        reply_markup=rsrkey
    )
    return


@Client.on_callback_query(regex("^unpin_all_in_this_chat$"))
async def unpinall_calllback(client, query):
    user_id = query.from_user.id
    user_status = (await query.message.chat.get_member(user_id)).status
    if not user_status in owner_status:
        await query.answer(
            "Group creator chauh in a ti thei",
            show_alert=True,
        )
        return
    try:
        await client.unpin_all_chat_messages(query.message.chat.id)
        await query.message.edit_text("Group a message pin awm zawng zawng te unpin vek a ni e.")
    except RightForbidden:
        await query.message.edit_text("Hetah message pin emaw unpin theihna permission ka neilo.")
    except MessageIdInvalid:
        await message.reply_text("**Message unpin tur ID hi ka hmu theilo.**")    
    return
