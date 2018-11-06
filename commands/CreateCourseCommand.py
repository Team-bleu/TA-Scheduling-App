from Command import Command
from CourseUtility import CourseUtility
from Command import Command


class CreateCourseCommand(Command):

    def action(self, user_input_list):
        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"
        
        courseUtil = CourseUtility()
        courseName = user_input_list[1]


        courseUtil.createCourse(courseName)


    def isCommand(self, command):
        return command == "createcourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
