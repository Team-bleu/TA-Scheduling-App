import unittest
from AssignCourseCommand import AssignCourseCommand

class AssignCourseCommandTest(unittest.TestCase):
    def setUp(self):
        self.cmd = AssignCourseCommand()
        self.user_input_list1 = ["assigncourse", "Peter", "CS250"]
        self.user_input_list2 = ["assigncourse", "Tom", "CS520"]
        self.user_input_list3 = ["assigncourse", "John", "CS351"]
        self.invalid_input_list = ["invalidCommand", "user"]

    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))

    def test_assign_course(self):
        pass


if __name__ == "__main__":
    unittest.main()
