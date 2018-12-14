from Command import Command
from CourseUtility import CourseUtility


class RemoveCourseCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 2:
            return "Do not have permission"

        # <course>
        courseUtil = CourseUtility()

        courseName = str(user_input_list[1]).upper()    # force uppercase

        if (courseUtil.getContents(courseName) == False):
            return courseName + " does not exist"

        courseUtil.deleteCourse()


        return courseName +" has been removed"



    def isCommand(self, command):
        return command == "removecourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2