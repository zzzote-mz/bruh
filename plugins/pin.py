# ©️2022 RSR
from pyrogram.errors import RightForbidden
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram.filters import regex
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("pin", prefixes=["/", "!"]))
@admins_only
async def pin_message(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    pin_args = message.text.split(None, 1)
    if message.reply_to_message:
        try:
            disable_notification = True

            if len(pin_args) >= 2 and pin_args[1] in ["loud"]:
                disable_notification = False

            await message.reply_to_message.pin(
                disable_notification=disable_notification,
            )

            if message.chat.username:
                link_chat_id = message.chat.username
                hmm = (
                    f"https://t.me/{link_chat_id}/{message.reply_to_message.message_id}"
                )
            elif (str(message.chat.id)).startswith("-100"):
                link_chat_id = (str(message.chat.id)).replace("-100", "")
                hmm = (
                    f"https://t.me/c/{link_chat_id}/{message.reply_to_message.message_id}"
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







@Client.on_message(filters.command("unpin", prefixes=["/", "!"]))
@admins_only
async def unpin_message(client, message):
    try:
        if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
        elif message.reply_to_message:
            await client.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
            await message.reply_text("**Message unpin ani e.**")
        else:
            await client.unpin_chat_message(message.chat.id)
            await message.reply_text("**Message pin hnu hnun ber unpin ani e.**")
    except RightForbidden:
        await m.reply_text("**Hetah message pin emaw unpin theihna permission ka neilo.**")
    
    return
                                     
                                     
                                     
@Client.on_message(filters.command("unpinall", prefixes=["/", "!"]))
@admins_only
async def unpinall_message(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    else:
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
    if user_status not in {"creator", "administrator"}:
        await query.answer(
            "Group creator chauh in a ti thei.",
            show_alert=True,
        )
        return
    if user_status != "creator":
        await query.answer(
            "Group creator chauh in a ti thei.",
            show_alert=True,
        )
        return
    try:
        await client.unpin_all_chat_messages(query.message.chat.id)
        await query.message.edit_text("Group a message pin awm zawng zawng te unpin vek ani e.")
    except RightForbidden:
        await query.message.edit_text("Hetah message pin emaw unpin theihna permission ka neilo.")
    return
