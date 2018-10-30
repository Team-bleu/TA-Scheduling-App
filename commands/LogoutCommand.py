from Command import Command
from user import User


class LogoutCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        if self.isCurrent():
            return self.logged()

        empty_user = User()
        self.setCurrent(empty_user)

        return "logged out."

    def isCommand(self, command):
        return command == "logout"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
