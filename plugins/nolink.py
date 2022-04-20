# ©️2022 RSR
from pyrogram import Client, filters
from Tereuhte.tetakte.helper import admins_only


@Client.on_message(filters.command("nolink", prefixes=["/", "!"]))
@admins_only
async def nolink(client, message):
    if message.chat.type == "private":
            await client.send_message(
                message.chat.id,
                text="**Hei chu group ah chauh a hman theih.**",
                reply_to_message_id=message.message_id
            )
            return
    elif not message.reply_to_message and len(message.command) == 1:
       await message.reply_text("**Command hmang hian i message delete sak duh leh warning nghal i duh message kha reply rawh.**")
       return
    elif message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        umen = message.reply_to_message.from_user.mention
        await message.reply_to_message.delete()
        await message.delete()
        await client.send_message(message.chat.id, text=f"Hello {umen}\n\nHe group ah hian Admin tan lo chuan link share phal anilo. Chuvang chuan i link rawn share kha delete ani. I link share duh kha a pawimawh a share i mamawh chuan Admin te private in dil la, Admin te kaltlang in an rem tih chuan i share thei ang.")
        return
