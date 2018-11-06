import unittest
from CreateLabCommand import CreateLabCommand
from LoginCommand import LoginCommand


class CreateLabTest(unittest.TestCase):

    def setUp(self):
        self.cmd = CreateLabCommand()
        self.user_input_list1 = ["createlab", "CS250", "lab01"]
        self.user_input_list2 = ["createlab","CS520", "lab01"]
        self.user_input_list3 = ["createlab", "CS351", "lab01"]
        self.invalid_input_list = ["createlab", "CS595"]
        self.invalid_input_list1 = ["Create", "CS251"]

    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list1))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertFalse(self.cmd.countArgs(self.user_input_list3))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list3[0]))

    def test_create_lab(self):
        # First, before we test adding a lab, we must make sure a
        # supervisor is already logged in (since they can add lab)
        LoginCommand.action(self.cmd, ["login", "super", "pass"])

        # Now we create a lab in TEST100 course
        # Make sure that TEST100 exists
        self.assertEqual(self.cmd.action(["createlab", "TEST100", "LAB801"]), "LAB801 has been created")
