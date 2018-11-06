import unittest
from LogoutCommand import LogoutCommand

class LogoutCommandTest(unittest.TestCase):

    def setUp(self):
        self.cmd = LogoutCommand()
        self.user_input_list = ["logout"]
        self.invalid_input_list = ["invalidArgument"]

    def test_invalid_input_list(self):
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))

    def test_logout_command(self):
        self.assertEqual(self.cmd.action(self.user_input_list), "logged out.")
