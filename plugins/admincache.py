from pyrogram import Client, filters
from Tereuhte.tetakte.cache import admin_cache_reload
from Tereuhte.tetakte.admins import admin_status
from pyrogram.enums import ChatMembersFilter






@Client.on_message(filters.command("admins", prefixes=["/", "!"]) & filters.group)
async def mentionadmins(client, message):
    mention = ""
    async for i in message.chat.get_members(
        message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        if not (i.user.is_deleted or i.privileges.is_anonymous):
            mention += f"➥ {i.user.mention}\n"
    await client.send_message(
        message.chat.id,
        text=("**{}** a Admin te chu:\n\n{}").format(message.chat.title, mention),
        reply_to_message_id=message.id
    )    
    
    
    
@Client.on_message(filters.command("admincache", prefixes=["/", "!"]) & filters.group)    
async def reload_admins(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    await admin_cache_reload(message, "admincache")
    await message.reply_text("**Admin list refresh ani e ✅**")
        
    
    
    
