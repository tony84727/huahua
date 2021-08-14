from eco.command import PingEcoCommand
from huahua.command import Commander, InlineDictParser
import unittest


class DummyCommand(Commander):
    pass


class CommanderTestCase(unittest.TestCase):

    def test_select_command(self):
        commander = Commander()
        command_a = DummyCommand()
        command_b = DummyCommand()
        commander.add_command("a", command_a)
        commander.add_command("b", command_b)
        self.assertEqual(command_a, commander.select_command('!a'))
        self.assertEqual(command_a, commander.select_command(
            '!a args1 args2 !args3'))
        self.assertEqual(command_b, commander.select_command('!b'))


class InlineDictParserTestCase(unittest.TestCase):
    def test_parse(self):
        cases = [
            {
                'input': '!ping address=example.com',
                'expected': {
                    'address': 'example.com',
                },
            },
            {
                'input': '!ping name="nice server"',
                'expected': {
                    'name': 'nice server',
                },
            },
            {
                'input': '!motd message=\'I say "YOOOOOO"\'',
                'expected': {
                    'message': 'I say "YOOOOOO"',
                },
            },
            {
                'input': 'a=1 b=\'hello world\' c=:)',
                'expected': {
                    'a': '1',
                    'b': 'hello world',
                    'c': ':)',
                }
            },
            {
                'input': "address='example.com' alias='latest'",
                'expected': {
                    'address': 'example.com',
                    'alias': 'latest',
                }
            }
        ]
        parser = InlineDictParser()
        for c in cases:
            with self.subTest(c['input']):
                self.assertEqual(c['expected'], parser.parse(c['input']))
