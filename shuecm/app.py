import logging

from vk import VK
from vk.bot_framework import Dispatcher
from vk.utils import TaskManager

from shuecm.config import VK_GROUP_ID
from shuecm.config import VK_TOKEN

logging.basicConfig(level="INFO")
vk = VK(VK_TOKEN)
dp = Dispatcher(vk, VK_GROUP_ID)


async def run():
    from shuecm.blueprints import info_bp

    dp.setup_blueprint(info_bp)

    dp.run_polling()


if __name__ == "__main__":
    manager = TaskManager(vk.loop)
    manager.add_task(run)
    manager.run()
