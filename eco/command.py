from eco.ping import PingResult, Pinger
from eco.formatting import discord_friendly_message
from huahua.command import Command
from discord import Colour
import discord
import time


def server_status_message(result: PingResult, spent=None):
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
        self.pinger = Pinger(server_address)

    async def execute(self, message: discord.Message):
        start = time.time()
        result = self.pinger.fetch()
        spent = round((time.time() - start) * 1000, 2)
        await message.reply(embed=server_status_message(result, spent))
