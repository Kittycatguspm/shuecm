"""
Registration middleware for shuecm.
"""
import logging

from vk.bot_framework import BaseMiddleware
from vk.types.events.community.event import MessageNew
from vk.utils.get_event import get_event_object

from shuecm.models.models.user import create_user
from shuecm.models.models.user import get_user
from shuecm.models.models.user import User

logger = logging.getLogger(__name__)


class RegistrationMiddleware(BaseMiddleware):
    """
    Register users in database if event == "message_new".
    """

    async def pre_process_event(self, event: dict, data: dict) -> dict:
        if event["type"] == "message_new":
            event: MessageNew = get_event_object(event)
            usr: User = await get_user(event.object.from_id)
            if usr:
                return data
            else:
                await create_user(uid=event.object.from_id)
                logger.info(
                    f"User with id ({event.object.from_id}) succesfully registered!"
                )
                await event.object.answer(
                    f"[id{event.object.from_id}| Пользователь] успешно зарегистрирован!"
                )
        return data

    async def post_process_event(self) -> None:
        pass
