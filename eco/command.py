from discord.embeds import Embed
from huahua.server import ServerList
from eco.ping import PingResult, Pinger
from eco.formatting import discord_friendly_message
from huahua.command import Command
from discord import Colour
import discord
import time
import re


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
                    result.total_players()), value="\n".join(result.players()) or "最高品質，靜悄悄")
    embed.add_field(name="版本", value=result.version())
    if spent != None:
        embed.set_footer(text=f"耗時 {spent} 毫秒")
    return embed


class PingEcoCommand(Command):
    """Ping command that report summary of the server status"""

    def __init__(self, server_list: ServerList) -> None:
        super().__init__()
        self.server_list = server_list

    async def execute(self, message: discord.Message):
        start = time.time()
        match = re.search('!ping\s*(.+)', message.content)
        alias = 'default'
        if match != None:
            alias = match[1].strip()
        server = await self.server_list.resolve(alias)
        if server is None:
            embed = Embed()
            embed.colour = Colour.red()
            embed.description = f"找不到 {alias} 伺服器"
            await message.reply(embed=embed)
        pinger = Pinger(server.address)
        result = pinger.fetch()
        spent = round((time.time() - start) * 1000, 2)
        await message.reply(embed=server_status_message(result, spent))
