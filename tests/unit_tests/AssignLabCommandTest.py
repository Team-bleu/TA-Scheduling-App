import unittest
from AssignLabCommand import AssignLabCommand

class AssignLabCommandTest(unittest.TestCase):
    def setUp(self):
        self.cmd = AssignLabCommand()
        self.user_input_list1 = ["assignlab", "Peter", "CS250", "lab01"]
        self.user_input_list2 = ["assignlab", "Tom", "CS520", "lab01"]
        self.user_input_list3 = ["assignlab", "John", "CS351", "lab01"]
        self.invalid_input_list = ["invalidCommand", "user", "class"]

    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))

    def test_assign_lab(self):
        pass