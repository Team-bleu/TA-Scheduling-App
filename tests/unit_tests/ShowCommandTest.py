import unittest
from ShowCommand import ShowCommand
from LoginCommand import LoginCommand

class ShowCommandTest(unittest.TestCase):

    def setUp(self):
        self.cmd = ShowCommand()
        self.invalid_input_list0 = ["show", "Peter"]
        self.invalid_input_list1 = ["view", "TA1"]
        self.valid_command0 = ["show", "TA1"]
        self.valid_command1 = ["show", "super"]
        self.login_command = ["login", "super", "pass"]
        self.string = "First Name: first\nLast Name: last\nemail: email\nphone: phone\naddress: address"

    def test_is_command(self):
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.valid_command0[0]))

    def test_role_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.valid_command1), self.string)


    def test_invalid_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.invalid_input_list0), "Peter doesn't exist!")
