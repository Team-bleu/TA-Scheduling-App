from django.test import TestCase
from AddCommand import AddCommand
from UserUtility import UserUtility
from LoginCommand import LoginCommand
from RemoveCommand import  RemoveCommand


class AddCommandTest(TestCase):
    util = UserUtility()

    def setUp(self):
        self.cmd = AddCommand()
        self.remCmd = RemoveCommand()
        self.remList = ["remove", "user1"]
        self.remList2 = ["remove", "user2"]
        self.user_input_list1 = ["add", "user1", "admin123"]
        self.user_input_list2 = ["add", "user2", "admin123"]
        self.user_input_list3 = ["add", "user3", "admin123"]
        self.invalid_input_list = ["invalidCommand", "user"]

    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertFalse(self.cmd.countArgs(self.user_input_list3))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list3[0]))

    # Before this line is initiated, make user user1 and user2
    # aren't existing users already. (This can occur if the test
    # is ran multiple times at once).
    def test_add_user(self):
        # First, before we test adding a user, we must make sure a
        # supervisor is already logged in (since they can add users)
        LoginCommand.action(self.cmd, ["login", "super", "pass"])

        # Now, we can start adding users.
        self.assertEqual(self.cmd.action(self.user_input_list1), "USER1 has been added")
        self.assertEqual(self.cmd.action(self.user_input_list1), "User already exists.")
        self.assertEqual(self.cmd.action(self.user_input_list2), "USER2 has been added")
        self.assertEqual(self.cmd.action(self.user_input_list2), "User already exists.")
        # Now we got to remove the users added so it doesn't crash the second run
        LoginCommand.action(self.remCmd, ["login", "super", "pass"])
        self.remCmd.action(self.remList)
        self.remCmd.action(self.remList2)
        #self.util.removeUser("USER1")
        #self.util.removeUser("USER2")



