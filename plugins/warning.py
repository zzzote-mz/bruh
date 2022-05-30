# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.admins import admin_status
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



rsrk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Warning sûtna", callback_data="close_i"
                    )
                ],
            ]
        )


@Client.on_message(filters.command("warn", prefixes=["/", "!"]) & filters.group)
async def warn(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if len(message.command) < 2:
        return await message.reply_text("Command zawh ah a chhan dah tel rawh.")
    if message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        zz = message.text.split(None, 1)[1]
        lal = await message.chat.get_member(uid)
        if lal.status in admin_status:
            return await message.reply_text(
                "Admin chu ka ban theilo."
            )
        umen = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {umen}\n**➥ID:** {uid}\n**➥A chhan:** {zz}", reply_markup=rsrk, reply_to_message_id=message.reply_to_message.id)
        return
    if len(message.command) == 1:
        await message.reply_text("Command hmang hian i warning duh message reply rawh. I warning chhan dah tel i duh chuan command zawh ah a chhan tur i dah dawn nia")
        return
    
    
    
    
@Client.on_message(filters.command("dwarn", prefixes=["/", "!"]) & filters.group)
async def dwarn(client, message):
    heh = message.from_user.id
    huh = await message.chat.get_member(heh)
    if not huh.status in admin_status:
        return await message.reply_text(
            "Admin i nih loh chuan i ti ve theilo."
        )
    if len(message.command) < 2:
        return await message.reply_text("Command zawh ah a chhan dah tel rawh.")
    if message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        zu = message.text.split(None, 1)[1]
        lal = await message.chat.get_member(uid)
        if lal.status in admin_status:
            return await message.reply_text(
                "Admin chu ka ban theilo."
            )
        umen = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {umen}\n**➥ID:** {uid}\n**➥A chhan:** {zu}", reply_markup=rsrk)
        await message.reply_to_message.delete()
        await message.delete()
        return
    if len(message.command) == 1:
        await message.reply_text("Command hmang hian i warning duh message reply rawh. I warning chhan dah tel i duh chuan command zawh ah a chhan tur i dah dawn nia")
        return  
    
    
    
    
