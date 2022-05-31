#ported from ultroid
#credits to ultroid

import os
import wget
import glob
import random
from pyrogram import filters, enums, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont


S = ( "https://telegra.ph/file/6110cc4791371b7240a30.jpg", "https://telegra.ph/file/128a9b1af071e0ff8b1b5.jpg", "https://telegra.ph/file/62718fd1f32650e438866.jpg", "https://telegra.ph/file/80c469bae35f630f2efe9.jpg", "https://telegra.ph/file/18b2d94d5de899bd25c8e.jpg", "https://telegra.ph/file/d2787e720928fc37501fe.jpg", "https://telegra.ph/file/54556616a157e0f9a43e2.jpg", "https://telegra.ph/file/64adf5ef91b5a611cc995.jpg", "https://telegra.ph/file/8e72c23a2fd042a078d81.jpg", "https://telegra.ph/file/88d959e9d22fe6f45c722.jpg", "https://telegra.ph/file/232a4f53a0a8fb06a4d82.jpg", "https://telegra.ph/file/8d2d3205887bd5abe1c2a.jpg", "https://telegra.ph/file/96a7130af1f8ee01586c9.jpg", "https://telegra.ph/file/5c72e5cede7949ae1e6e9.jpg", "https://telegra.ph/file/b8b3ca8208a4e543d61de.jpg", "https://telegra.ph//file/87af3475150eee832402d.jpg", "https://telegra.ph//file/9e848a13cfab0611b3e63.jpg", "https://telegra.ph//file/1adb8ca9f3f558612ff00.jpg")
 
 
@Client.on_message(filters.command("clogo", prefixes=["/", "!"]))
async def logo(client, message):
 if len(message.command) < 2:
    await client.send_message(message.chat.id, text="I logo hming tur dah tel rawh.", reply_to_message_id=message.id)
    return
 text = message.text.split(None, 1)[1]
 lol = await client.send_message(message.chat id, text="`Logo siam mek a ni e...`", reply_to_message_id=message.id,)
 fpath = glob.glob("Botfiles/Fonts/*")
 font_ = random.choice(fpath)
 oho = random.choice(S)
 pics = wget.download(oho)

 if len(text) <= 8:
     fnt_size = 150
     strke = 10
 elif len(text) >= 9:
      fnt_size = 50
      strke = 5
 else:
     fnt_size = 130
     strke = 20

 img = Image.open(pics)
 draw = ImageDraw.Draw(img)
 font = ImageFont.truetype(font_, fnt_size)
 w, h = draw.textsize(text, font=font)
 h += int(h * 0.21)
 image_width, image_height = img.size
 draw.text(
     ((image_width - w) / 2, (image_height - h) / 2),
     text,
     font=font,
     fill=(255, 255, 255),
 )
 x = (image_width - w) / 2
 y = (image_height - h) / 2
 draw.text(
     (x, y), text, font=font, fill="white", stroke_width=strke, stroke_fill="black"
  )
 file_name = 'RSR.png'
 rsrke = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Siamtu", url="https://t.me/tlangvaltea_bot"
                    )
                ],
            ]
        )
 await client.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
 img.save(file_name, "png")
 if message.reply_to_message:
         await client.send_photo(
             message.chat.id,
             photo=file_name,
             reply_markup=rsrke,
             reply_to_message_id=message.reply_to_message.id,
         )
         await lol.delete()
 else:
     await client.send_photo(
         message.chat.id, photo=file_name, reply_markup=rsrke, reply_to_message_id=message.id,
     ),
     await lol.delete()
     if os.path.exists(file_name):
         os.remove(file_name)
