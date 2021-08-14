import re
from typing import Mapping, Optional
from discord import Message


class Command:
    """Command represents a bot command"""

    def execute(self, message: Message):
        """execute the command"""
        pass


class Commander(Command):
    def __init__(self):
        self.commands: Mapping[str, Command] = {}
        self.command_parsing_pattern = re.compile('!(\S+)')

    def add_command(self, name: str, command: Command):
        self.commands[name] = command

    def execute(self, message: Message):
        selected = self.select_command(message.content)
        if selected != None:
            selected.execute(message)

    def select_command(self, message_text: str) -> Optional[Command]:
        match = self.command_parsing_pattern.search(message_text)
        if match is None:
            return
        return self.commands.get(match[1])
