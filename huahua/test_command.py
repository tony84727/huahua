from huahua.command import Commander
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
