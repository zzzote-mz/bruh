#ported from ultroid
#credits to ultroid

import os
import wget
import glob
import random
from pyrogram import filters, enums, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont


S = ( "https://telegra.ph//file/111fd979e87e9f42f2c19.jpg", "https://telegra.ph//file/bfc0b1f66bf5a8b2c574c.jpg", "https://telegra.ph//file/cd2d1696620339084624c.jpg", "https://telegra.ph//file/bfc0b1f66bf5a8b2c574c.jpg", "https://telegra.ph//file/9ab646f7cf3c126495fbe.jpg", "https://telegra.ph//file/32456d888874c75ed29ee.jpg", "https://telegra.ph//file/c60bc9d86aa541a4df3dd.jpg", "https://telegra.ph//file/548ad05d1b525f523f321.jpg", "https://telegra.ph//file/2e6d3c6e3e4e674d5c0df.jpg", "https://telegra.ph//file/87af3475150eee832402d.jpg", "https://telegra.ph//file/a5b6ec4221d9bcc191c7d.jpg", "https://telegra.ph//file/d7003a9ce86a9b1f874a0.jpg", "https://telegra.ph//file/8226be18c2202cd1769e1.jpg", "https://telegra.ph//file/c4cddc6bd4977d6fd0915.jpg", "https://telegra.ph//file/81f30d3778e3045ebaac0.jpg", "https://telegra.ph//file/592ef483d76dcb7b1f8a1.jpg", "https://telegra.ph//file/2a0db95a8abc2b463437d.jpg", "https://telegra.ph//file/9e848a13cfab0611b3e63.jpg", "https://telegra.ph//file/1adb8ca9f3f558612ff00.jpg", "https://telegra.ph//file/ab0e4b42cf57a77ed58b3.jpg", "https://telegra.ph//file/e3bcad1d7bc01cb5372cc.jpg", "https://telegra.ph//file/c275505d38b8373fb8391.jpg", "https://telegra.ph//file/de62b9753f6689a7bfc77.jpg", "https://telegra.ph//file/dfd4074f97aa65742c25b.jpg", "https://telegra.ph//file/d188ad5fe891110ed8817.jpg", "https://telegra.ph//file/01bdfd9e85356862fd073.jpg", "https://telegra.ph//file/4dda10ab3bc3e02b4a3db.jpg", "https://telegra.ph//file/b8e13cd5ad49adcba46c0.jpg", "https://telegra.ph//file/b87d6bfdfdae591f45194.jpg", "https://telegra.ph//file/73a6ac7d3a3f040f85cdf.jpg", "https://telegra.ph//file/a4a04eebb4e221756245f.jpg", "https://telegra.ph//file/d2f6c27c471b451553be4.jpg", "https://telegra.ph//file/ed7f1f3139161cfe0ed7c.jpg", "https://telegra.ph//file/98709b420a05e58a4a1d5.jpg", "https://telegra.ph//file/0819127d4bf204b442d03.jpg", "https://telegra.ph//file/c5b54f42e7e0d9f6845c0.jpg", "https://telegra.ph//file/4b934457155bb60b10e6d.jpg", "https://telegra.ph//file/c31c37db2f7599829fcdc.jpg", "https://telegra.ph//file/e26c4f5e617056631032e.jpg", "https://telegra.ph//file/e36a163b460fb3c4b1692.jpg", "https://telegra.ph//file/b79604dfe25fcaff9bf4c.jpg", "https://telegra.ph//file/45caa3f45d7ed06a4b3ad.jpg", "https://telegra.ph//file/e5ee9ec14bb2868624a0b.jpg", "https://telegra.ph//file/0ce7f065eab79ab9d81fe.jpg", "https://telegra.ph//file/37bc0c69374182d707d94.jpg", "https://telegra.ph//file/79f5b1b6d02f556963c4a.jpg", "https://telegra.ph//file/9f5a8e68a11495d5aa985.jpg", "https://telegra.ph//file/9e3b72b58927e13af6f46.jpg", "https://telegra.ph//file/137fc30c4605701fb65ea.jpg", "https://telegra.ph//file/7f16afd5b2a176a2d4057.jpg", "https://telegra.ph//file/bfafc5ab6c603b52f7677.jpg", "https://telegra.ph//file/e38cce2ba228bfd47e0ae.jpg", "https://telegra.ph//file/95fb15423efd9826d7d50.jpg", "https://telegra.ph//file/5bcb0f847784c02951662.jpg", "https://telegra.ph//file/2b18905814111143fd471.jpg", "https://telegra.ph//file/536d6cd8d6c841f76c9a9.jpg", "https://telegra.ph//file/01bb952ca835c0a7fec07.jpg")
 
 
@Client.on_message(filters.command("ilogo", prefixes=["/", "!"]))
async def logo(client, message):
 text = message.text.split(None, 1)[1]
 lol = await message.reply_text("`Logo siam mek a ni e...`")
 if  not text:
    await lol.edit("I logo hming tur dah tel rawh.")
    return
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
 rsrk = InlineKeyboardMarkup(
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
             reply_markup=rsrk,
             reply_to_message_id=message.reply_to_message.id,
         )
         await lol.delete()
 else:
     await client.send_photo(
         message.chat.id, photo=file_name, reply_markup=rsrk,
     ),
     await lol.delete()
     if os.path.exists(file_name):
         os.remove(file_name)
