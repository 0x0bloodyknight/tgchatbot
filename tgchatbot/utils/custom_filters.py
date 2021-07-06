from pyrogram import filters

import config as config

master_chat_filter = filters.create(
    lambda _, __, query: query.chat.id == config.master_chat_id)
