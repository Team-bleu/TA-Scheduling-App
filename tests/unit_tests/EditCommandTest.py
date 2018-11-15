import unittest
from EditCommand import EditCommand
from LoginCommand import LoginCommand


class EditCommandTest(unittest.TestCase):
    def setUp(self):
        self.cmd = EditCommand()
        self.invalid_input_list0 = ["edit", "Peter"]
        self.invalid_input_list1 = ["set", "TA1"]
        self.valid_command0 = ["edit", "TA1", "firstname", "John"]
        self.valid_command1 = ["edit", "TA1", "firstname", "Eddard", "lastname", "stark", "address", "222 MaryLand"]
        self.login_command = ["login", "super", "pass"]

    def test_is_command(self):
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.valid_command0[0]))

    def test_role_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.valid_command0), "information updated")
        self.assertEqual(self.cmd.action(self.valid_command1), "information updated")

    def test_invalid_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.invalid_input_list0), "Peter doesn't exist!")
