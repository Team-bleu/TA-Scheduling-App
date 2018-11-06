import unittest
from CreateCourseCommand import CreateCourseCommand


class CreateCourseTest(unittest.TestCase):

    def setUp(self):
        self.cmd = CreateCourseCommand()
        self.user_input_list1 = ["createcourse", "CS250"]
        self.user_input_list2 = ["createcourse","CS520"]
        self.user_input_list3 = ["createcourse", "CS351"]
        self.invalid_input_list = ["createcourse"]
        self.invalid_input_list1 = ["Create", "CS251"]


    def test_invalid_input_list(self):
        self.assertTrue(self.cmd.countArgs(self.invalid_input_list))
        self.assertFalse(self.cmd.isCommand(self.invalid_input_list1[0]))

    def test_valid_input_list(self):
        self.assertFalse(self.cmd.countArgs(self.user_input_list1))
        self.assertFalse(self.cmd.countArgs(self.user_input_list2))
        self.assertFalse(self.cmd.countArgs(self.user_input_list3))
        self.assertTrue(self.cmd.isCommand(self.user_input_list1[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list2[0]))
        self.assertTrue(self.cmd.isCommand(self.user_input_list3[0]))

    def test_create_course(self):
        pass