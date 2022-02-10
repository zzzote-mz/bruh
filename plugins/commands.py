import os
import logging
import random
import asyncio
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp
import re
import json
import base64
logger = logging.getLogger(__name__)

BATCH_FILES = {}

@Client.on_message(filters.command("start") & filters.incoming & ~filters.edited)
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('Help', url=f"https://t.me/{temp.U_NAME}?start=help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(message.chat.id, text="Hello {}, a hnuaia **Help** tih button khu hmet la start rawh, chuan private lam ah a pawimawh dang chu i en thei ang.".format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_to_message_id=message.message_id, reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('Help', callback_data='help')
            ],[
            InlineKeyboardButton('Helpline', url='https://t.me/helptereuhte'),
            InlineKeyboardButton('Channel', url='https://t.me/rsrbots')
            ],[
            InlineKeyboardButton('Developer', user_id='1060318977'),
            InlineKeyboardButton('About', callback_data='about')
            ],[
            InlineKeyboardButton('Share', url='https://t.me/share/url?url=Mizo%20%E1%B9%ADawnga%20lehlin%20movie%20%E1%B9%ADhenkhat%20zawn%20na%20leh%20en%20na%20hi%20i%20hman%20ve%20duh%20chuan%20a%20hnuaia%20Bot%20tia%20ka%20kawh%20na%20zawn%20a%20username%20khu%20hmet%20la%20i%20hmang%20thei%20ang%2C%20a%20free%20vek%20in.%0A%0ABot%20%F0%9F%91%89%20%40mzmvbot')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(
            message.chat.id,
            text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_to_message_id=message.message_id,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "Join", url=invite_link.invite_link
                )
            ]
        ]

        await client.send_message(
            chat_id=message.from_user.id,
            text="Min hman duh chuan a hnuaia **Join** tih button hi hmet la join rawh, channel member te chauh in min hmang thei.",
            reply_to_message_id=message.message_id,
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
        )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
            InlineKeyboardButton('Help', callback_data='help')
            ],[
            InlineKeyboardButton('Helpline', url='https://t.me/helptereuhte'),
            InlineKeyboardButton('Channel', url='https://t.me/rsrbots')
            ],[
            InlineKeyboardButton('Developer', user_id='1060318977'),
            InlineKeyboardButton('About', callback_data='about')
            ],[
            InlineKeyboardButton('Share', url='https://t.me/share/url?url=Mizo%20%E1%B9%ADawnga%20lehlin%20movie%20%E1%B9%ADhenkhat%20zawn%20na%20leh%20en%20na%20hi%20i%20hman%20ve%20duh%20chuan%20a%20hnuaia%20Bot%20tia%20ka%20kawh%20na%20zawn%20a%20username%20khu%20hmet%20la%20i%20hmang%20thei%20ang%2C%20a%20free%20vek%20in.%0A%0ABot%20%F0%9F%91%89%20%40mzmvbot')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(
            message.chat.id,
            text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_to_message_id=message.message_id,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    file_id = message.command[1]
    if file_id.split("-", 1)[0] == "BATCH":
        sts = await message.reply("Please wait")
        file_id = file_id.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await client.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
            os.remove(file)
            BATCH_FILES[file_id] = msgs
        for msg in msgs:
            title = msg.get("title")
            size=get_size(int(msg.get("size", 0)))
            f_caption=msg.get("caption", "")
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{title}"
            await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=msg.get("file_id"),
                caption=f_caption,
                )
        await sts.delete()
        return
    elif file_id.split("-", 1)[0] == "DSTORE":
        sts = await message.reply("Please wait")
        b_string = file_id.split("-", 1)[1]
        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")
        f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)
        msgs_list = list(range(int(f_msg_id), int(l_msg_id)+1))
        for msg in msgs_list:
            try:
                await client.copy_message(chat_id=message.chat.id, from_chat_id=int(f_chat_id), message_id=msg)
            except Exception as e:
                logger.exception(e)
                pass  
        return await sts.delete()

    files_ = await get_file_details(file_id)           
    if not files_:
        try:
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id
                )
            filetype = msg.media
            file = getattr(msg, filetype)
            title = file.file_name
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            await msg.edit_caption(f_caption)
            return
        except:
            pass
        return await message.reply('File hmuh anilo.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return
    
    file_id, file_ref = unpack_new_file_id(media.file_id)

    result = await Media.collection.delete_one({
        '_id': file_id,
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
        result = await Media.collection.delete_one({
            'file_name': file_name,
            'file_size': media.file_size,
            'mime_type': media.mime_type
            })
        if result.deleted_count:
            await msg.edit('File is successfully deleted from database')
        else:
            # files indexed before https://github.com/EvamariaTG/EvaMaria/commit/f3d2a1bcb155faf44178e5d7a685a1b533e714bf#diff-86b613edf1748372103e94cacff3b578b36b698ef9c16817bb98fe9ef22fb669R39 
            # have original file name.
            result = await Media.collection.delete_one({
                'file_name': media.file_name,
                'file_size': media.file_size,
                'mime_type': media.mime_type
            })
            if result.deleted_count:
                await msg.edit('File is successfully deleted from database')
            else:
                await msg.edit('File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCEL", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('Succesfully Deleted All The Indexed Files.')
