from django.test import TestCase
from CreateCourseCommand import CreateCourseCommand
from RemoveCourseCommand import RemoveCourseCommand
from LoginCommand import LoginCommand
from CourseUtility import CourseUtility



class RemoveCourseTest(TestCase):

    def setUp(self):
        self.cmd0 = CreateCourseCommand()
        self.cmd = RemoveCourseCommand()
        self.user_input_list1 = ["removecourse", "CS250"]
        self.user_input_list2 = ["removecourse","CS520"]
        self.user_input_list3 = ["removecourse", "CS351"]
        self.invalid_input_list = ["removecourse"]
        self.invalid_input_list1 = ["RemoveCourses", "CS251"]
        self.courseUtil = CourseUtility()


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
        # First, before we test adding a course, we must make sure a
        # supervisor is already logged in (since they can add courses)
        LoginCommand.action(self.cmd0, ["login", "super", "pass"])
        self.assertEquals(self.cmd0.action(["createcourse", "TEST100"]), "TEST100 has been created")

        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEquals(self.cmd.action(["removecourse", "TEST100"]), "TEST100 has been removed")

    def test_create_course_error(self):

        self.assertEquals(self.cmd.action(["removecourse", "TEST100"]), "No user is logged in.")
        LoginCommand.action(self.cmd, ["login", "super", "pass"])
        self.assertEquals(self.cmd.action(["removecourse", "TEST100"]), "TEST100 does not exist")


