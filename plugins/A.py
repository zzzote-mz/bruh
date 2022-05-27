# ©️2022 RSR

from pyrogram import Client, filters



@Client.on_message(filters.command("ban", prefixes=["/", "!"]) & filters.private)
async def ban(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("unban", prefixes=["/", "!"]) & filters.private)
async def unban(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("remove", prefixes=["/", "!"]) & filters.private)
async def remove(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("setgtitle", prefixes=["/", "!"]) & filters.private)
async def setgtitle(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("setgpic", prefixes=["/", "!"]) & filters.private)
async def setgpic(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("delgpic", prefixes=["/", "!"]) & filters.private)
async def delgpic(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("removeme", prefixes=["/", "!"]) & filters.private)
async def removeme(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("close", prefixes=["/", "!"]) & filters.private)
async def close(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("open", prefixes=["/", "!"]) & filters.private)
async def open(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("mute", prefixes=["/", "!"]) & filters.private)
async def mute(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("unmute", prefixes=["/", "!"]) & filters.private)
async def unmute(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("dmute", prefixes=["/", "!"]) & filters.private)
async def dmute(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("pin", prefixes=["/", "!"]) & filters.private)
async def pin(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("unpin", prefixes=["/", "!"]) & filters.private)
async def unpin(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("unpinall", prefixes=["/", "!"]) & filters.private)
async def unpinall(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("fpromote", prefixes=["/", "!"]) & filters.private)
async def fpromote(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("lpromote", prefixes=["/", "!"]) & filters.private)
async def lpromote(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("demote", prefixes=["/", "!"]) & filters.private)
async def demote(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("title", prefixes=["/", "!"]) & filters.private)
async def title(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return




@Client.on_message(filters.command("mban", prefixes=["/", "!"]) & filters.private)
async def mban(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return




@Client.on_message(filters.command("setdescription", prefixes=["/", "!"]) & filters.private)
async def sdescription(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


@Client.on_message(filters.command("admincache", prefixes=["/", "!"]) & filters.private)
async def admincache(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return





@Client.on_message(filters.command("dban", prefixes=["/", "!"]) & filters.private)
async def dban(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return




@Client.on_message(filters.command("warn", prefixes=["/", "!"]) & filters.private)
async def warn(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return




@Client.on_message(filters.command("dwarn", prefixes=["/", "!"]) & filters.private)
async def dwarn(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return




@Client.on_message(filters.command("tetakte", prefixes=["/", "!"]) & filters.private)
async def tereuhte(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("protect", prefixes=["/", "!"]) & filters.private)
async def protect(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return



@Client.on_message(filters.command("zombies", prefixes=["/", "!"]) & filters.private)
async def zombies(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return




@Client.on_message(filters.command("admins", prefixes=["/", "!"]) & filters.private)
async def admins(client, message):
    await client.send_message(
        message.chat.id,
        text="**Hei chu group ah chauh a hman theih.**",
        reply_to_message_id=message.id
    )
    return


