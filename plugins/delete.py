from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only



@Client.on_message(filters.command("dltall", prefixes=["/", "!"]) & filters.group)
@admins_only
async def spurge(client, message):
    if message.chat.type != "supergroup":
        await message.reply_text("Supergroup ami chiah ka delete thei.")
        return

    if message.reply_to_message:
        message_ids = list(range(message.reply_to_message.message_id, message.message_id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        # Dielete messages in chunks of 100 messages
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=plist,
                    revoke=True,
                )
            await message.delete()
        except MessageDeleteForbidden:
            await message.reply_text("I message delete duh hi ka delete theilo, a chhan chu message hi a hlui tawh ani thei(ni 2 liam tawh message ka delete theilo. Chuan supergroup ami lo chu ka delete theilo, emaw hemi group ah hian message delete theihna permission ka neilo pawh ani thei. A khawi emaw ber vang hian i message delete duh hi ka delete theilo.")
            return
        except RPCError as ef:
            await message.reply_text(
                   "Message delete theih anilo, harsatna thlen i duh chuan @helptereuhte ah i sawi thei ang.",
                    ef=ef,
            )
        return
    else:
        await message.reply_text("Command hmang hian i delete duhna chin a message reply rawh.")
        return
    
    
    
    
    
@Client.on_message(filters.command("dlt", prefixes=["/", "!"]) & filters.group)
@admins_only    
async def dlt(client, message):
    if message.chat.type != "supergroup":
        return

    if message.reply_to_message:
        await message.delete()
        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=message.reply_to_message.message_id,
        )
    else:
        await message.reply_text("I message delete duh reply rawh.")
    return   
    
    
