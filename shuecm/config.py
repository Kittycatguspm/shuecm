from environs import Env

env: Env = Env()
env.read_env()

VK_TOKEN = env("VK_TOKEN")
VK_GROUP_ID = env.int("VK_GROUP_ID")
