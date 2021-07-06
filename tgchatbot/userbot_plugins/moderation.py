from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember

import utils.custom_filters as custom_filters
import utils.logger as logger


@Client.on_message(
    filters.command('purge') & custom_filters.master_chat_filter)
async def purge(client: Client, message: Message):
    try:
        to_message_id = message.reply_to_message.message_id
        from_message_id = message.message_id
    except Exception:
        await message.reply_text('Reply to message')
        return

    user: ChatMember = await client.get_chat_member(
        message.chat.id,
        message.from_user.id,
    )

    if not user.status in ['administrator', 'creator']:
        await message.reply_text('Administrators only')
        return
    if not user.can_delete_messages:
        await message.reply_text(
            'You don\'t have permission to delete messages')
        return

    count = 0
    if await client.delete_messages(message.chat.id,
                                    range(to_message_id, from_message_id)):
        count += from_message_id - to_message_id

    for i in range(from_message_id - 1, to_message_id + 1, -1):
        if await client.delete_messages(message.chat.id, i):
            count += 1

    await client.send_message(
        message.chat.id,
        f'Done!\nPurged ≈{count} messages',
    )
    await logger.log('purge', message, client)
