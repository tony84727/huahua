import re
from typing import Mapping, Optional
from discord import Message


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
