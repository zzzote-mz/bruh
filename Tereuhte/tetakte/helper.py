from typing import Callable, Coroutine, List



async def get_administrators(chat: Chat) -> List[User]:
    _get = get(chat.id)

    if _get:
        return _get
    else:
        set(
            chat.id,
            [member.user for member in await chat.get_members(filter="administrators")],
        )
        return await get_administrators(chat)


def admins_only(func: Callable) -> Coroutine:
    async def wrapper(client: Client, message: Message):
        if message.from_user.id == OWNER_ID:
            return await func(client, message)
        admins = await get_administrators(message.chat)
        for admin in admins:
            if admin.id == message.from_user.id:
                return await func(client, message)
            if not admin.id == message.from_user.id:
                await message.reply_text("**Admin inih loh chuan iti ve theilo.**")
                return

    return wrapper
