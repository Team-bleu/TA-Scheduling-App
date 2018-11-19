from Command import Command
from CourseUtility import CourseUtility


class CreateLabCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"

        courseUtil = CourseUtility()
        courseName = user_input_list[1]
        labName = user_input_list[2]

        if (courseUtil.getContents(courseName) == False):   #if course doesn't exist, return error
            return courseName + " does not exist"

        if (courseUtil.createLab(labName) == False):
            return labName + " already exists"
        courseUtil.writeContents()

        return labName + " has been created"


    def isCommand(self, command):
        return command == "createlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
