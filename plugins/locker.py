# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only
from pyrogram.types import ChatPermissions

@Client.on_message(filters.command("close", prefixes=["/", "!"]))
@admins_only
async def close(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    else:
        await client.set_chat_permissions(chat_id=message.chat.id, permissions=ChatPermissions())
        await client.send_message(message.chat.id, text="**Group ah hian member tan message thawn theihloh tura siam ani e.**", reply_to_message_id=message.message_id)
        return
      
@Client.on_message(filters.command("open", prefixes=["/", "!"]))
@admins_only
async def open(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    else:
        await client.set_chat_permissions(
            chat_id=message.chat.id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_invite_users=True,
                can_add_web_page_previews=True
            )
          
        )
        await client.send_message(message.chat.id, text="**Group ah hian member tan paw'n message thawn thei tura siam ani e.**", reply_to_message_id=message.message_id)
        return     
      
