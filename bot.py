from huahua.command import Commander
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
        self.commander = Commander()
        self.commander.add_command(
            'ping', PingEcoCommand(must_env('ECO_SERVER')))

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        if message.author.bot or not message.content.startswith('!ping'):
            return
        await self.commander.execute(message)


client = MyClient()

if __name__ == '__main__':
    client.run(must_env('TOKEN'))
