# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status
from pyrogram.types import ChatPermissions

@Client.on_message(filters.command("close", prefixes=["/", "!"]) & filters.group)
async def close(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    await client.set_chat_permissions(chat_id=message.chat.id, permissions=ChatPermissions())
    await client.send_message(message.chat.id, text="**Group ah hian member tan message thawn theih loh tura siam ani e.**", reply_to_message_id=message.id)
    return
      
@Client.on_message(filters.command("open", prefixes=["/", "!"]) & filters.group)
async def open(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    await client.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_invite_users=True,
            can_add_web_page_previews=True,
            can_send_polls=True
        )
    )
    await client.send_message(message.chat.id, text="**Group ah hian member tan paw'n message thawn theih tura siam ani e.**", reply_to_message_id=message.id)
    return     
      
