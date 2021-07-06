import asyncio

from pyrogram import Client, filters, idle

import config as config

userbot = Client(
    'userbot_account',
    api_id=config.api_id,
    api_hash=config.api_hash,
    plugins=dict(root='userbot_plugins'),
    workdir='sessions',
)

bot = Client(
    'bot_account',
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token,
    plugins=dict(root='bot_plugins'),
    workdir='sessions',
)

userbot.start()
bot.start()

idle()

bot.stop()
userbot.stop()
