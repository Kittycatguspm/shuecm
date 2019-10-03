import asyncio

import umongo
from motor.motor_asyncio import AsyncIOMotorClient
from vk.utils import ContextInstanceMixin

from shuecm.config import MONGODB_CONNECTION_URI
from shuecm.config import MONGODB_DATABASE_NAME


class DB(ContextInstanceMixin):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.client = AsyncIOMotorClient(MONGODB_CONNECTION_URI)
        self.db = self.client[MONGODB_DATABASE_NAME]

        self.set_current(self)


class Instance(ContextInstanceMixin):
    """
    uMongo DB instance.
    """

    def __init__(self, db: DB = None):
        if not db:
            self.db = DB.get_current().db
        else:
            self.db = db

        self.instance = umongo.Instance(self.db)

        self.set_current(self)


db = DB()
instance = Instance()
