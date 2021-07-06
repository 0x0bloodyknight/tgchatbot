import asyncio

from pyrogram import Client, filters, types
from pyrogram.types import Message

import utils.custom_filters as custom_filters
import utils.logger as logger
import utils.cas as cas


@Client.on_message(
    filters.new_chat_members
    & custom_filters.master_chat_filter, )
async def greet(client: Client, message: Message):
    await logger.log('new_chat_member', message, client)

    user = message.new_chat_members[0]
    if await should_ban(user):
        await client.kick_chat_member(message.chat.id, user.id)
        await logger.log('kicked_new_chat_member', message, client)
        await message.delete()
        return

    welcome_gif_file_id = 'CgACAgQAAx0CRuS6OAABA5vNYMvSu8E8b3yKnHVqWYS0B4xMfF8AAksCAAJWxERTXuW3p4UkVh0eBA'
    greeting = await message.reply_animation(
        welcome_gif_file_id,
        caption=f'Hello {user.mention}!',
    )
    await asyncio.sleep(60)
    await greeting.delete()
    await message.delete()


async def should_ban(user: types.User):
    if user.id >= 1700000000:
        return True
    if await cas.check_ban(user.id):
        return True
