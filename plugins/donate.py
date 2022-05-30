from pyrogram import filters
from pyrogram import Client 



@Client.on_message(filters.command("donate", prefixes=["/", "!"]))
async def donate(client, message):
  await client.forward_messages(message.chat.id, from_chat_id=-1001640035413, message_ids=30)
  await client.send_message(message.chat.id, text="A chunga Donate tih button hi hmet la min ṭanpui na'n i donate thei ang. Emaw, a hnuaia link hi join la, tah khan donate dan chi dang deuh pawh a en theih ang.\n\nhttps://t.me/teamtereuhte", reply_to_message_id=message.id, disable_web_page_preview=True)
  return
