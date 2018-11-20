import unittest
from QuitCommand import QuitCommand

class QuitCommandTest(unittest.TestCase):

    def setUp(self):
        self.cmd = QuitCommand()
        self.invalid_input_list = ["invalidArgument"]
        self.valid_command = ["quit"]

    def test_is_command(self):
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))
        self.assertTrue(self.cmd.isCommand(self.valid_command[0]))

    def test_quit_command(self):
        self.assertEqual(self.cmd.action(self.valid_command), "Quiting session.")