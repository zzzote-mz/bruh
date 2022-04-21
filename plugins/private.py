# ©️2022 RSR

from pyrogram import Client, filters



@Client.on_message(filters.command("mute", prefixes=["/", "!"]) & filters.private)
