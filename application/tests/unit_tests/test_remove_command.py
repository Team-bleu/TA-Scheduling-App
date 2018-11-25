from django.test import TestCase
from RemoveCommand import RemoveCommand
from LoginCommand import LoginCommand
from AddCommand import AddCommand

class RemoveCommandTest(TestCase):

    def setUp(self):
        self.cmd = RemoveCommand()
        self.addCmd = AddCommand()
        self.invalid_input_list0 = ["remove", "Peter"]
        self.invalid_input_list1 = ["delete", "TA1"]
        self.valid_command0 = ["remove", "TA1"]
        self.valid_command1 = ["remove", "user1"]
        self.login_command = ["login", "super", "pass"]
        self.user_input_list1 = ["add", "user1", "admin123"]

    def test_is_command(self):
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.valid_command0[0]))

    def test_role_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.addCmd, ["login", "super", "pass"])
        self.assertEqual(self.addCmd.action(self.user_input_list1), "user1 has been added")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.valid_command1), "user1 has been removed.")
        self.assertEqual(self.cmd.action(self.valid_command1), "user1 doesn't exist!")


    def test_invalid_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.invalid_input_list0), "Peter doesn't exist!")
