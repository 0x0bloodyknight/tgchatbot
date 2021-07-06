import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.errors.exceptions.flood_420 import FloodWait

import utils.custom_filters as custom_filters


@Client.on_message(
    filters.command(['change_avatar', 'lol'])
    & custom_filters.master_chat_filter)
async def set_random_avatar(client: Client, message: Message):
    members = await client.get_chat_members(message.chat.id, filter='all')
    random_member: User = random.choice(members).user
    while random_member.photo is None:
        random_member: User = random.choice(members).user

    try:
        photo_file_path = await client.download_media(
            random_member.photo.big_file_id)
        await client.set_chat_photo(message.chat.id, photo=photo_file_path)
    except FloodWait as e:
        response = await message.reply(str(e))
        await asyncio.sleep(10)
        await message.delete()
        await response.delete()
        return

    seen = False
    async for message_ in client.iter_history(message.chat.id, limit=100):
        if message_.service:
            if hasattr(message_, 'new_chat_photo'):
                if seen:
                    await message_.delete()
                    break
                seen = True
