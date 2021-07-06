import aiohttp
import asyncio


async def check_ban(user_id: int):
    is_banned = False
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://api.cas.chat/check?user_id={user_id}') as response:
            response_json = await response.json()
            if response_json['ok']:
                is_banned = True
    return is_banned


if __name__ == '__main__':
    asyncio.run(check_ban(1585802207))
