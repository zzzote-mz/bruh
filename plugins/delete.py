from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status



@Client.on_message(filters.command("dltall", prefixes=["/", "!"]) & filters.group)
async def spurge(client, message):
    #if message.chat.type != "supergroup":
        #await message.reply_text("Supergroup ami chiah ka delete thei.")
        #return
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if message.reply_to_message:
        message_ids = list(range(message.reply_to_message.id, message.id))

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
            await message.reply_text("I message delete duh hi ka delete theilo, zawh chian duh emaw harsatna i neih chuan @helptereuhte ah hian i sawi thei ang.")
            return
        except RPCError as ef:
            await message.reply_text(
                   "Message delete theih a nilo, harsatna thlen i duh chuan @helptereuhte ah i sawi thei ang.",
                    ef=ef,
            )
        return
    else:
        await message.reply_text("Command hmang hian i delete duhna chin a message reply rawh.")
        return
    
    
    
    
    
@Client.on_message(filters.command("dlt", prefixes=["/", "!"]) & filters.group)
async def dlt(client, message):
    #if message.chat.type != "supergroup":
        #return
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if message.reply_to_message:
        await message.delete()
        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=message.reply_to_message.id,
        )
    else:
        await message.reply_text("I message delete duh reply rawh.")
    return   
    
    
