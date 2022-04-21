# ©️2022 RSR

from pyrogram import Client, filters



@Client.on_message(filters.command("ban", prefixes=["/", "!"]) & filters.private)
async def ban(client, message):
    await client.send_message(message.chat.id, text="**Hei chu group ah chauh a hman theih.**",
