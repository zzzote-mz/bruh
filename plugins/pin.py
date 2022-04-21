# ©️2022 RSR




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
                                    "Invite Friends", url="https://t.me/share/url?url=Mizo%20Mobile%20Legend%20khel%20%E1%B9%ADhin%20te%20tan%20group%20siam%20ania%2C%20i%20khel%20ve%20a%2C%20i%20join%20ve%20duh%20anih%20chuan%20a%20hnuai%20a%20join%20tia%20ka%20kawh%20na%20a%20username%20khu%20click%20in%20i%20join%20thei%20ang.%0A%0AJoin%20%F0%9F%91%89%20%40mizoml"
                                   ),
                                ],
                            ]
                        )
            await message.reply_text(
                "**He message hi ka pin e.**",
            )

        except ChatAdminRequired:
            await m.reply_text(tlang(m, "admin.not_admin"))
        except RightForbidden:
            await m.reply_text(tlang(m, "pin.no_rights_pin"))
        except RPCError as ef:
            await m.reply_text(
                (tlang(m, "general.some_error")).format(
                    SUPPORT_GROUP=SUPPORT_GROUP,
                    ef=ef,
                ),
            )
            LOGGER.error(ef)
    else:
        await m.reply_text("Reply to a message to pin it!")

    return
