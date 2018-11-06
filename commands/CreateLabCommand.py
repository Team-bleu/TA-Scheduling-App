from Command import Command
from CourseUtility import CourseUtility
from Command import Command


class CreateLabCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

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
