from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


async def spurge(c: Alita, m: Message):
    if m.chat.type != "supergroup":
        await m.reply_text(tlang(m, "purge.err_basic"))
        return

    if m.reply_to_message:
        message_ids = list(range(m.reply_to_message.message_id, m.message_id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        # Dielete messages in chunks of 100 messages
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await c.delete_messages(
                    chat_id=m.chat.id,
                    message_ids=plist,
                    revoke=True,
                )
            await m.delete()
        except MessageDeleteForbidden:
            await m.reply_text(tlang(m, "purge.old_msg_err"))
            return
        except RPCError as ef:
            await m.reply_text(
                (tlang(m, "general.some_error")).format(
                    SUPPORT_GROUP=SUPPORT_GROUP,
                    ef=ef,
                ),
            )
        return
    await m.reply_text("Reply to a message to start spurge !")
    return
