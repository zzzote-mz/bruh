# ©️2022 RSR
from pyrogram.errors import RightForbidden
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram.filters import regex


@Client.on_message(filters.command("pin", prefixes=["/", "!"]))
@admins_only
async def pin_message(client, message):
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
        if messags.reply_to_message:
            await client.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
            await m.reply_text("**Message unpin ani e.**)
        else:
            await client.unpin_chat_message(message.chat.id)
            await message.reply_text("**Message pin hnu hnun ber unpin ani e."")
    except RightForbidden:
        await m.reply_text("**Hetah message pin emaw unpin theihna permission ka neilo.**")
    
    return
                                     
                                     
                                     
@Client.on_message(filters.command("unpinall", prefixes=["/", "!"]))
@admins_only
async def unpinall_message(client, message):
    await message.reply_text(
        "**Group a message pin zawng zawng hi unpin vek i duh tih i chiang maw?**",
        reply_markup=ikb([[("Yes", "unpin_all_in_this_chat"), ("No", "close_admin")]]),
    )
    return


@Alita.on_callback_query(regex("^unpin_all_in_this_chat$"))
async def unpinall_calllback(c: Alita, q: CallbackQuery):
    user_id = q.from_user.id
    user_status = (await q.message.chat.get_member(user_id)).status
    if user_status not in {"creator", "administrator"}:
        await q.answer(
            "You're not even an admin, don't try this explosive shit!",
            show_alert=True,
        )
        return
    if user_status != "creator":
        await q.answer(
            "You're just an admin, not owner\nStay in your limits!",
            show_alert=True,
        )
        return
    try:
        await c.unpin_all_chat_messages(q.message.chat.id)
        LOGGER.info(f"{q.from_user.id} unpinned all messages in {q.message.chat.id}")
        await q.message.edit_text(tlang(q, "pin.unpinned_all_msg"))
    except ChatAdminRequired:
        await q.message.edit_text(tlang(q, "admin.notadmin"))
    except RightForbidden:
        await q.message.edit_text(tlang(q, "pin.no_rights_unpin"))
    except RPCError as ef:
        await q.message.edit_text(
            (tlang(q, "general.some_error")).format(
                SUPPORT_GROUP=SUPPORT_GROUP,
                ef=ef,
            ),
        )
        LOGGER.error(ef)
    return
