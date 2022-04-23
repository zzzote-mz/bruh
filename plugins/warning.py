# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


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
@admins_only
async def warn(client, message):
    if message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        uvu = await client.get_users(uid)
        if uvu.status == "administrator":
            await message.reply_text("Admin ka warning theilo")
        umen = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {umen}\n**➥ID:** {uid}\n**➥A chhan:** Awmlo", reply_to_message_id=message.reply_to_message.message_id)
        return
    if message.reply_to_message and len(message.command) == 2:
        zz = message.text.split(None, 1)[1]
        zx = message.reply_to_message.from_user.id
        xc = await client.get_users(zx)
        if xc.status == "administrator":
            await message.reply_text("Admin ka earning theilo")
        zc = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {zc}\n**➥ID:** {zx}\n**➥A chhan:** {zz}", reply_to_message_id=message.reply_to_message.message_id)
        return
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i warning duh message reply rawh. I warning chhan dah tel i duh chuan command zawh ah a chhan tur i dah dawn nia")
        return
    
    
    
    
@Client.on_message(filters.command("dwarn", prefixes=["/", "!"]) & filters.group)
@admins_only
async def dwarn(client, message):
    if message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        uvu = await client.get_users(uid)
        if uvu.status == "administrator":
            await message.reply_text("Admin ka warning theilo")
        umen = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {umen}\n**➥ID:** {uid}\n**➥A chhan:** Awmlo")
        await message.reply_to_message.delete()
        await message.delete()
        return
    if message.reply_to_message and len(message.command) == 2:
        zz = message.text.split(None, 1)[1]
        zx = message.reply_to_message.from_user.id
        xc = await client.get_users(zx)
        if xc.status == "administrator":
            await message.reply_text("Admin ka earning theilo")
        zc = message.reply_to_message.from_user.mention
        await client.send_message(message.chat.id, text=f"**❗ Warning**\n\n**➥User:** {zc}\n**➥ID:** {zx}\n**➥A chhan:** {zz}")
        await message.reply_to_message.delete()
        await message.delete()
        return
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text("Command hmang hian i warning duh message reply rawh. I warning chhan dah tel i duh chuan command zawh ah a chhan tur i dah dawn nia")
        return  
    
    
    
    
