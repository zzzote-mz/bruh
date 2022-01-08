from pyrogram import filters
from pyrogram import Client 



@Client.on_message(filters.command('tell'))
async def tell(client, message):
  rsr3 = message.text.split(None, 1)[1]
  if message.reply_to_message:
                             await client.send_messages(chat_id=rsr3, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                             await message.reply_text("<b>✅ Ka thawn zo e.</b>", parse_mode="html")
