import asyncio
from typing import List, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import User, Post, async_engine, Base, Session



async def get_users_posts_data():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    return users_data, posts_data



async def add_users(session: AsyncSession, users_data: List[Dict]):
    users = [
        User(
            name=user_data.get("name"),
            username=user_data.get("username"),
            email=user_data.get("email")
        )
        for user_data in users_data
    ]
    session.add_all(users)
    await session.commit()



async def add_posts(session: AsyncSession, posts_data: List[Dict]):
    posts = [
        Post(
            title=post_data.get("title"),
            body=post_data.get("body"),
            user_id=post_data.get("userId")
        )
        for post_data in posts_data
    ]
    session.add_all(posts)
    await session.commit()



async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with Session() as session:
        users_data, posts_data = await get_users_posts_data()
        await add_users(session, users_data)
        await add_posts(session, posts_data)



def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()