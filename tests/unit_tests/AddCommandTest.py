import unittest
from AddCommand import AddCommand


class AddCommandTest(unittest.TestCase):

    def setUp(self):
        self.cmd = AddCommand()
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
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))

    # Before this line is initiated, make user user1 and user2
    # aren't existing users already. (This can occur if the test
    # is ran multiple times at once).
    def test_add_user(self):
        self.assertEqual(self.cmd.action(self.user_input_list1, "", "", ""), "user1 has been added")
        self.assertEqual(self.cmd.action(self.user_input_list1, "", "", ""), "User already exists.")
        self.assertEqual(self.cmd.action(self.user_input_list2, "", "", ""), "user2 has been added")
        self.assertEqual(self.cmd.action(self.user_input_list2, "", "", ""), "User already exists.")


if __name__ == "__main__":
    unittest.main()
