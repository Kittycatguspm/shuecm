"""
Blueprint for informational commands.
"""
from vk import types
from vk.bot_framework.dispatcher import Blueprint

bp = Blueprint()


@bp.message_handler(text="инфа")
async def info_handler(message: types.Message, data: dict):
    await message.answer("Тестовое сообщение!")
