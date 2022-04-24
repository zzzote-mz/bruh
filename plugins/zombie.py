import asyncio
import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@pbot.on_message(filters.command("zombies", prefixes=["/", "!"]) & filters.group)
@admins_only
async def zombie(client, message):
    pablo = await message.reply_text("**Zawng mek...**")
    if len(message.text.split()) == 1:
        dm = 0
        da = 0
        dc = 0
        async for member in client.iter_chat_members(message.chat.id):
            if member.user.is_deleted:
                await sleep(1)
                if member.status == "member":
                    dm += 1
                elif member.status == "administrator":
                    da += 1
                elif member.status == "creator":
                    dc += 1
        text = "**📊 Zombies Stats** \n\n"
        if dm > 0:
            text += "**Zombies (Members) :** `{}` \n".format(dm)
        if da > 0:
            text += "\n**Zombies (Admins) :** `{}` \n".format(da)
        if dc > 0:
            text += "\n*:Zombie account hi Creator ani.**\n"
        d = dm + da + dc
        if d > 0:
            text += "\n\n`/zombies clean` tih hmang hian account delete te i remove thei ang."
            await pablo.edit(text)
        else:
            await pablo.edit("**Group ah hian account delete a awmlo.**")
        return
    sgname = message.text.split(None, 1)[1]
    user_id = message.from_user.id
    if sgname.lower().strip() == "clean":
        lol = await message.chat_get_member(user_id)
        if lol.status not in {"creator", "administrator"}:
            await pablo.edit("**Admin inih loh chuan iti ve theilo.**")
            return
        s = 0
        f = 0
        async for member in client.iter_chat_members(message.chat.id):
            if member.user.is_deleted:
                try:
                    await client.ban_chat_member(message.chat.id, member.user.id)
                    s += 1
                except:
                    f += 1
        text = "🧟‍♂️"
        if s > 0:
            text += "**Account Delete** {} **Remove ani.**".format(s)
        if f > 0:
            text += "\n\n**Account Delete remove theihloh** {} **a awm, Admin emaw Creator an nih vang ani maithei.**".format(f)
        await pablo.edit(text)
    else:
        await pablo.edit("**He mi group ah hian account delete a awmlo.**")
    return
