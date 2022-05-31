# © @Mr_Dark_Prince
import aiohttp
from pyrogram import filters, Client




@Client.on_message(filters.command("github", prefixes=["/", "!"]))
async def github(client, message):
    if len(message.command) != 2:
        await client.send_message(message.chat.id, text="Command zawh ah github username dah rawh", reply_to_message_id=message.id)
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await client.send_message(message.chat.id, text="**Error:** 404", reply_to_message_id=message.id)
            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**{name} Info:**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Siam hun:** `{created_at}`
**Repository:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Follow tu:** `{followers}`
**Follow te:** `{following}`"""
            except Exception as e:
                print(e)
    await client.send_photo(message.chat.id, photo=avatar_url, caption=caption, reply_to_message_id=message.id)
