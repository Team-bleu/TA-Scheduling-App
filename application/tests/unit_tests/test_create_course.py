from django.test import TestCase
from CreateCourseCommand import CreateCourseCommand
from LoginCommand import LoginCommand
from CourseUtility import CourseUtility
import os


class CreateCourseTest(TestCase):

    def setUp(self):
        self.cmd = CreateCourseCommand()
        self.user_input_list1 = ["createcourse", "CS250"]
        self.user_input_list2 = ["createcourse","CS520"]
        self.user_input_list3 = ["createcourse", "CS351"]
        self.invalid_input_list = ["createcourse"]
        self.invalid_input_list1 = ["Create", "CS251"]
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
        LoginCommand.action(self.cmd, ["login", "super", "pass"])

        if os.path.isfile("data/courses/TEST100.txt"):
            self.assertEquals(self.cmd.action(["createcourse", "TEST100"]), "Course already exists")

        else:
            # If this test is failing:
            # We have to manually delete TEST100.txt from data/courses/ if
            # it's been created prior or already exist so this test can run correctly
            self.assertEquals(self.cmd.action(["createcourse", "TEST100"]), "TEST100 has been created")
            self.courseUtil.getContents("TEST100")
            self.courseUtil.deleteCourse()


