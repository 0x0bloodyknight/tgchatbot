import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

import utils.custom_filters as custom_filters
import config as config


async def log(log_type: str, message: Message, client: Client):
    log_hash = log_type
    log_content = await resolve_type(log_type, message)
    await client.send_message(
        config.log_chat_id,
        f'''
        #{log_hash}
        {log_content}
        ''',
    )


async def resolve_type(log_type: str, message: Message):
    # TODO: implement resolve_type in logger.py
    # if log_type == 'purge':
    #     pass
    # elif log_type == 'new_chat_member':
    #     pass
    # elif log_type == 'kicked_new_chat_member':
    #     pass

    return f'```{str(message)}```'
