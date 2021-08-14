import re
from typing import Dict, Mapping, Optional
from discord import Message
import discord
from discord.colour import Colour
from discord.embeds import Embed
from sqlalchemy.sql.expression import desc
from huahua.server import AliasConflictException, ServerList
from model import Server


class Command:
    """Command represents a bot command"""

    async def execute(self, message: Message):
        """execute the command"""
        pass


class Commander(Command):
    """
        Act like a Command, but also a command selector.
        Allow users to register command. When executed as a command, the Command select the proper command
        to execute. If there're no matched command, it's a no-op.
    """

    def __init__(self):
        self.commands: Mapping[str, Command] = {}
        self.command_parsing_pattern = re.compile('!(\S+)')

    def add_command(self, name: str, command: Command):
        self.commands[name] = command

    async def execute(self, message: Message):
        selected = self.select_command(message.content)
        if selected != None:
            await selected.execute(message)

    def select_command(self, message_text: str) -> Optional[Command]:
        match = self.command_parsing_pattern.search(message_text)
        if match is None:
            return
        return self.commands.get(match[1])


def remove_quote(text: str) -> str:
    """Remove outer quote"""
    if text[0] == text[-1] and (text[0] == '\'' or text[0] == '\"'):
        return text[1:-1]
    return text


class InlineDictParser:
    """
        Used to parse arguments in "inline dictionary" form

        For example:
        "a=1 b='hello world'"
        will be parsed as a dictionary:
        {
            'a': '1',
            'b': 'hello world',
        }
    """

    def __init__(self) -> None:
        self.entry_extract_pattern = re.compile(
            r'(\S+)\s*=\s*([^\s\'"]+|([\'"]).*?\3)')

    def parse(self, input: str) -> Dict:
        """Parse the argument and return a dictionary"""
        dict = {}
        for match in self.entry_extract_pattern.finditer(input):
            dict[match[1]] = remove_quote(match[2])
        return dict


class AddServerCommand(Command):
    """Command for registering server"""

    def __init__(self, server_list: ServerList):
        super().__init__()
        self.server_list = server_list
        self.inline_dict_parser = InlineDictParser()

    async def execute(self, message: discord.Message):
        print(message.content)
        dict = self.inline_dict_parser.parse(message.content)
        print(dict)
        address = dict.get('address')
        if address is None:
            await message.reply('address參數為必填')
            return
        alias = dict.get('alias')
        description = dict.get('description')
        server = Server(address=address, alias=alias, description=description)
        try:
            await self.server_list.add(server)
        except AliasConflictException:
            embed = Embed()
            embed.description = f"無法新增伺服器, 別名：{alias} 已存在"
            return await message.reply(embed=embed)

        embed = Embed()
        embed.description = '已新增伺服器'
        embed.colour = Colour.green()
        embed.add_field(name='位址', value=address)
        embed.add_field(name='別名', value=alias)
        embed.add_field(name='說明', value=description)
        return await message.reply(embed=embed)


class ListServerCommand(Command):
    """Command for listing registered servers"""

    def __init__(self, server_list: ServerList) -> None:
        super().__init__()
        self.server_list = server_list

    async def execute(self, message: Message):
        list = "\n".join(
            [f"{s.alias!r}\t{s.address!r}\t{s.description!r}" for s in await self.server_list.all()])
        return await message.reply(list)
