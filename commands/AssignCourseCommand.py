from Command import Command
from CommandsList import CommandsList


class AssignCourseCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        if not CommandsList.getCredentialss() >= 4:
            return "Error. Current User does not have permission to assign course."

    def isCommand(self, command):
        return command == "assigncourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
