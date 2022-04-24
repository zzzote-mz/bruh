from pyrogram import filters
from pyrogram import Client 



@Client.on_message(filters.command("rsr", prefixes=["/", "!"]))
def donate(client, message):
  client.send_message(message.chat.id, text="A hnuaia **Website** tih button khu hmet la min siamtu website i en thei ang.", reply_to_message_id=message.message_id, disable_web_page_preview=True)
  return
