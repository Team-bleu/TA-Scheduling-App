from Command import Command
from CourseUtility import CourseUtility


class CreateCourseCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        
        courseUtil = CourseUtility()
        courseName = user_input_list[1]


        courseUtil.createCourse(courseName)


    def isCommand(self, command):
        return command == "createcourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
