from sqlalchemy.sql.sqltypes import Numeric
from huahua.command import Command, Commander
from eco.formatting import discord_friendly_message
import discord
import os
import time

from discord.colour import Colour
import eco


def must_env(name: str) -> str:
    v = os.environ.get(name)
    if v is None:
        print('please specify {} environment variable'.format(name))
        exit(-1)
    return v


def server_status_message(result: eco.ping.PingResult, spent=None):
    """format eco server ping result into a discord embed message"""
    embed = discord.Embed()
    embed.colour = Colour.green()
    embed.set_thumbnail(url='https://wiki.play.eco/logo.png')
    embed.add_field(
        name="名稱", value=discord_friendly_message(result.description()))
    embed.add_field(name="描述", value=discord_friendly_message(
        result.detailed_description()))
    embed.add_field(name="在線玩家 {}/{}".format(len(result.players()),
                    result.total_players()), value="\n".join(result.players()))
    embed.add_field(name="版本", value=result.version())
    if spent != None:
        embed.set_footer(text=f"耗時 {spent} 毫秒")
    return embed


class PingEcoCommand(Command):
    """Ping command that report summary of the server status"""

    def __init__(self, server_address: str) -> None:
        super().__init__()
        self.pinger = eco.ping.Pinger(server_address)

    async def execute(self, message: discord.Message):
        start = time.time()
        result = self.pinger.fetch()
        spent = round((time.time() - start) * 1000, 2)
        await message.reply(embed=server_status_message(result, spent))


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
