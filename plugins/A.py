from pyrogram import filters
from pyrogram import Client 
from info import ADMINS


@Client.on_message(filters.command('req'))
async def report(client, message):
  rsr = message.text.split(None, 1)[1]
  await client.send_message(chat_id=ADMINS, text=f"<b>⭕️Request⭕️\n\n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>\n<b>🧿 Req:</b> rsr")
  await client.send_message(message.chat.id, text="<b>✅ I request chu min siamtu hnen ah thawn ani e.</b>", reply_to_message_id=message.message_id)

        
