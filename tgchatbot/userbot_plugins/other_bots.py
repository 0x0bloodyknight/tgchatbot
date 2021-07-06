import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid

import utils.custom_filters as custom_filters
import config as config


@Client.on_message(
    filters.command(['created', 'creation_date'])
    & custom_filters.master_chat_filter)
async def creation_date(client: Client, message: Message):
    try:
        user_id = message.reply_to_message.from_user.id
    except Exception as e:
        await message.reply_text('Reply to message')
        return

    creation_date_bot_username = 'creationdatebot'

    request = await client.send_message(
        creation_date_bot_username,
        f'/id {user_id}',
    )
    expected_response_id = request.message_id + 1

    await asyncio.sleep(1)
    try:
        await client.forward_messages(
            config.master_chat_id,
            creation_date_bot_username,
            expected_response_id,
        )
    except MessageIdInvalid:
        await message.reply_text('Creation bot hasn\'t responded')
