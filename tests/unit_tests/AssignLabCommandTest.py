import unittest
from AssignLabCommand import AssignLabCommand
from LoginCommand import LoginCommand


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
        # First, before we test assigning a lab, we must make sure a
        # supervisor is already logged in (since they can assign labs)
        LoginCommand.action(self.cmd, ["login", "super", "pass"])

        # Now we can assign our dummy user a the lab section 801
        # from TEST100 course, make sure that the course and lab exists
        self.assertEqual(self.cmd.action(["assignlab", "TA1", "TEST100", "LAB801"]), "TA1 has been assigned to LAB801")
