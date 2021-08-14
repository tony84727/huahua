from db import new_engine
from huahua.server import DatabaseServerList
from huahua.command import AddServerCommand, Commander, ListServerCommand
from eco.command import PingEcoCommand
import discord
import os


def must_env(name: str) -> str:
    v = os.environ.get(name)
    if v is None:
        print('please specify {} environment variable'.format(name))
        exit(-1)
    return v


class MyClient(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        engine = new_engine()
        server_list = DatabaseServerList(engine)
        self.commander = Commander()
        self.commander.add_command(
            'ping', PingEcoCommand(server_list))
        self.commander.add_command('addserver', AddServerCommand(server_list))
        self.commander.add_command(
            'listserver', ListServerCommand(server_list))

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        await self.commander.execute(message)


client = MyClient()

if __name__ == '__main__':
    client.run(must_env('TOKEN'))
