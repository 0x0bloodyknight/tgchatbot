from pyrogram import Client, filters
from pyrogram.types import Message

import utils.custom_filters as custom_filters


@Client.on_message(
    filters.command('file_id') & custom_filters.master_chat_filter)
async def send_file_id(client: Client, message: Message):
    file_id = ''
    try:
        file_id = message.reply_to_message.photo.file_id
    except Exception:
        try:
            file_id = message.reply_to_message.animation.file_id
        except Exception:
            await message.reply('Reply to photo/gif')
    await message.reply(file_id)
