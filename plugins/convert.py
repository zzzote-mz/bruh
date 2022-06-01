import os
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Tereuhte.tetakte.helper import runcmd


@Client.on_message(filters.command("convert", prefixes=["/", "!"]))
async def convert(client, message):
  op = await client.send_message(message.chat.id, text="`Convert mek a ni...`", reply_to_message_id=message.id)
  format = message.text.split(None, 1)[1]
  if len(message.command) == 1:
    await op.edit("`Audio format dah tel rawh`\n\n**Entirnan:** mp3, m4a...etc")
    return
  if not message.reply_to_message:
    await op.edit("`Video reply rawh.`")
    return
  if not message.reply_to_message.video:
    await op.edit("`Audio a ka convert tur video reply rawh.`")
    return
  lol = message.reply_to_message
  kk = await client.download_media(lol)
  
  audio = str(os.path.basename(kk)).split(".")[0] + str(f".{format}")
  
  c_time = time.time()
  cmd = f"ffmpeg -i {kk} -map 0:a {audio}"

  ok = await runcmd(cmd)
  filem = audio
  if not os.path.exists(filem):
      await op.edit("**Ka convert theilo.**")
      return
  rsrkeyboar = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Siamtu", url="https://t.me/tlangvaltea_bot"
                    )
                ],
            ]
        )
  await client.send_audio(
      message.chat.id,
      audio=filem,
      progress_args=(
          op,
          c_time,
          str(audio)
      ),
      reply_markup=rsrkeyboar,
      reply_to_message_id=message.reply_to_message.id,
  )
  await op.delete()
  os.remove(filem)
