# ©️2022 RSR

from pyrogram import Client, filters



@Client.on_message(filters.command("ban", prefixes=["/", "!"]) & filters.private)
async def ban(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return



@Client.on_message(filters.command("unban", prefixes=["/", "!"]) & filters.private)
async def unban(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return


@Client.on_message(filters.command("remove", prefixes=["/", "!"]) & filters.private)
async def remove(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return


@Client.on_message(filters.command("setgtitle", prefixes=["/", "!"]) & filters.private)
async def setgtitle(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return


@Client.on_message(filters.command("setgpic", prefixes=["/", "!"]) & filters.private)
async def setgpic(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return



@Client.on_message(filters.command("delgpic", prefixes=["/", "!"]) & filters.private)
async def delgpic(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return


@Client.on_message(filters.command("removeme", prefixes=["/", "!"]) & filters.private)
async def removeme(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.message_id
    )
    return
