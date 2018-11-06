import unittest
from AssignCourseCommand import AssignCourseCommand
from LoginCommand import LoginCommand


class AssignCourseCommandTest(unittest.TestCase):
    def setUp(self):
        self.cmd = AssignCourseCommand()
        self.user_input_list1 = ["assigncourse", "Peter", "CS250"]
        self.user_input_list2 = ["assigncourse", "Tom", "CS520"]
        self.user_input_list3 = ["assigncourse", "John", "CS351"]
        self.invalid_input_list = ["invalidCommand", "user"]
        self.invalid_input_list1 = ["assign", "John", "CS351"]

    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertFalse(self.cmd.countArgs(self.user_input_list3))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list3[0]))

    def test_assign_course(self):
        # Before we can test whether or not we can add a course,
        # we must first log in a supervisor who has the role to do so
        LoginCommand.action(self.cmd, ["login", "super", "pass"])

        # Next, we will use the dummy user to assign it a course
        self.assertEqual(self.cmd.action(["assicncourse", "TA1", "TEST100"]), "TA1 has been assigned to TEST100")
