from django.test import TestCase
from RoleCommand import RoleCommand
from LoginCommand import LoginCommand
from application import app

class RoleCommandTest(TestCase):

    def setUp(self):
        self.cmd = RoleCommand()
        self.log = LoginCommand()
        self.invalid_input_list0 = ["role", "Peter", "TA"]
        self.invalid_input_list1 = ["assign", "TA1", "TA"]
        self.invalid_input_list2 = ["role", "TA1", "staff"]
        self.valid_command0 = ["role", "TA1", "TA"]
        self.valid_command1 = ["role", "TA1", "Instructor"]
        self.login_command = ["login", "super", "pass"]

        self.app = app.App()

    def test_is_command(self):
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.valid_command0[0]))

    def test_role_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.app.command("login super pass")
        self.app.command("add TA1 pass")
        self.assertEqual(self.cmd.action(self.valid_command1), "TA1 has become a Instructor")
        self.assertEqual(self.cmd.action(self.valid_command0), "TA1 has become a TA")
        self.app.command("remove TA1")

    def test_invalid_command(self):
        self.assertEqual(self.cmd.action(self.valid_command0), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEqual(self.cmd.action(self.invalid_input_list2), "staff doesn't exist!")
        self.assertEqual(self.cmd.action(self.invalid_input_list0), "Peter doesn't exist!")
