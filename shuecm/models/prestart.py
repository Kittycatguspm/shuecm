"""
Ensure indexes, etc.
"""
import asyncio

from .models.user import User


async def populate_db():
    await User.ensure_indexes()


def pre_start(loop: asyncio.AbstractEventLoop):
    loop.create_task(populate_db())
