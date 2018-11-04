import unittest
from LoginCommand import LoginCommand

class LoginCommandTest(unittest.TestCase):

    def setUp(self):
        self.cmd = LoginCommand()
        self.user_input_list1 = ["login", "user1", "admin123"]
        self.user_input_list2 = ["login", "user2", "wrongPassWord"]
        self.user_input_list3 = ["login", "user3", "admin123"]
        self.invalid_input_list = ["invalidCommand", "user"]

    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))

    def test_login_command(self):
        self.assertEqual(self.cmd.action(self.user_input_list1), "user1 logged in.")
        self.assertEqual(self.cmd.action(self.user_input_list2), "Wrong password.")
        self.assertEqual(self.cmd.action(self.user_input_list3), "No such user exists.")
