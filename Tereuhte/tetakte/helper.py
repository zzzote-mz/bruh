import shlex
import asyncio
from typing import Callable, Coroutine, List, Union, Dict, Tuple
from pyrogram.types import Chat, Message, User
from pyrogram import Client
from functools import wraps



admins: Dict[str, List[User]] = {}


def set(chat_id: Union[str, int], admins_: List[User]):
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    admins[chat_id] = admins_


def get(chat_id: Union[str, int]) -> Union[List[User], bool]:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    if chat_id in admins:
        return admins[chat_id]

    return False



async def get_administrators(chat: Chat) -> List[User]:
    if _get := get(chat.id):
        return _get
    set(
        chat.id,
        (
            member.user
            for member in await chat.get_members(filter="administrators")
        ),
    )

    return await get_administrators(chat)


def admins_only(func: Callable) -> Coroutine:
    async def wrapper(client: Client, message: Message):
        if message.from_user.id == 1060318977:
            return await func(client, message)
        admins = await get_administrators(message.chat)
        for admin in admins:
            if admin.id == message.from_user.id:
                return await func(client, message)
            await message.reply_text("**Admin inih loh chuan iti ve theilo.**")
            return

    return wrapper




async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

