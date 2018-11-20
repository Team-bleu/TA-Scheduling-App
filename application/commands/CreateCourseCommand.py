from Command import Command
from CourseUtility import CourseUtility


class CreateCourseCommand(Command):

    def action(self, user_input_list):
        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"
        
        courseUtil = CourseUtility()
        courseName = user_input_list[1]

        if (courseUtil.createCourse(courseName) == False):
            return courseName + " already exists"

        return courseName + " has been created"


    def isCommand(self, command):
        return command == "createcourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
