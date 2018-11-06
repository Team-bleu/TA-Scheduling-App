from Command import Command
from CourseUtility import CourseUtility
from CommandsList import CommandsList


class CreateLabCommand(Command):

    def action(self, user_input_list):
        if not CommandsList.getCredentialss() >= 4:
            return "Error. Current User does not have permission to create a lab."

        courseUtil = CourseUtility()
        courseName = user_input_list[1]
        labName = user_input_list[2]

        if (courseUtil.getContents(courseName) == False):   #if course doesn't exist, return error
            return

        courseUtil.createLab(labName)
        courseUtil.writeContents()


    def isCommand(self, command):
        return command == "createlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
