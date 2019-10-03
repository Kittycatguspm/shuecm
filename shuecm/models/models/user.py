import typing

import umongo
from umongo import fields

from shuecm.models.db import Instance

instance: umongo.Instance = Instance.get_current().instance


@instance.register
class User(umongo.Document):  # noqa
    """
    User document in database
    """

    uid = fields.IntegerField(required=True, unique=True)

    class Meta:
        collection = instance.db.users


async def create_user(uid: int) -> typing.Optional[typing.NoReturn]:
    """
    Create user in database or raise exception. - umongo.exceptions.UMongoError
    :param uid:
    :return:
    """
    user = User(uid=uid)
    await user.commit()


async def get_user(uid: int) -> typing.Union[User, typing.NoReturn]:
    """
    Lookup user in database via UID.
    :param uid:
    :return:
    """
    user = await User.find_one({"uid": uid})
    if not user:
        return  # check this state such as: if not user: return await message.answer("something..")
    return user
