"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data() -> list[dict]:
    async with ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
            users = await response.json()
    return users


async def fetch_posts_data() -> list[dict]:
    async with ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:
            posts = await response.json()
    return posts
