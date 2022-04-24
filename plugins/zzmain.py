# ©️2022 RSR
import logging
import asyncio
from pyrogram import Client, filters
logger = logging.getLogger(__name__)


@Client.on_message(filters.command("start", prefixes=["/", "!"]) & filters.private)
async def gstart(client, message):
    await client.send_video(message.chat.id, video="https://telegra.ph/file/96b84705d3c1cfc51b0aa.mp4", reply_to_message_id=message.id, protect_content=True)
    await asyncio.sleep(3)
    await client.send_message(message.chat.id, text="Hello, Bot hi siam lai mek ania, ala hman theih rihloh.")
    return
