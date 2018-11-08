from UserUtility import UserUtility
from Command import Command


class EditCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"

        util = UserUtility()
        username = user_input_list[1]
        user = util.searchUser(username)
        if user is None:
            return username + " doesn't exist!"

        pass

    def isCommand(self, command):
        return command == "edit"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
