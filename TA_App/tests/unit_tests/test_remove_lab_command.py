from django.test import TestCase
from CreateLabCommand import CreateLabCommand
from RemoveCourseCommand import RemoveCourseCommand
from CreateCourseCommand import CreateCourseCommand
from RemoveLabCommand import RemoveLabCommand
from LoginCommand import LoginCommand


class RemoveLabTest(TestCase):

    def setUp(self):
        self.cmd = RemoveLabCommand()
        self.cmd0 = CreateCourseCommand()
        self.cmd1 = CreateLabCommand()
        self.cmd2 = RemoveCourseCommand()
        self.user_input_list1 = ["removelab", "CS250", "lab01"]
        self.user_input_list2 = ["removelab","CS520", "lab01"]
        self.user_input_list3 = ["removelab", "CS351", "lab01"]
        self.invalid_input_list = ["removelab", "CS595"]
        self.invalid_input_list1 = ["RemoveLab", "CS251"]

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

        LoginCommand.action(self.cmd0, ["login", "super", "pass"])
        self.assertEquals(self.cmd0.action(["createcourse", "TEST100"]), "TEST100 has been created")

        LoginCommand.action(self.cmd2, ["login", "super", "pass"])
        self.assertEquals(self.cmd2.action(["removecourse", "TEST100"]), "TEST100 has been removed")

    def test_create_lab_error(self):
        self.assertEquals(self.cmd.action(["removelab", "TEST100", "lab01"]), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEquals(self.cmd.action(["removelab", "TEST100", "lab01"]), "TEST100 does not exist")

