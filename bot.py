from eco.formatting import discord_friendly_message
import discord
import os

from discord.colour import Colour
import eco


def must_env(name: str) -> str:
    v = os.environ.get(name)
    if v is None:
        print('please specify {} environment variable'.format(name))
        exit(-1)
    return v


def server_status_message(result: eco.ping.PingResult):
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
    return embed


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.pinger = eco.ping.Pinger(must_env('ECO_SERVER'))

    async def on_message(self, message: discord.Message):
        if message.author.bot or not message.content.startswith('!ping'):
            return
        result = self.pinger.fetch()
        await message.reply(embed=server_status_message(result))


client = MyClient()

if __name__ == '__main__':
    client.run(must_env('TOKEN'))
