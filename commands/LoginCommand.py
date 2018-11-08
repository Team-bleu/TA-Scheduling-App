from Command import Command
from UserUtility import UserUtility


class LoginCommand(Command):

    def action(self, user_input_list):
        util = UserUtility()
        username = user_input_list[1]
        password = user_input_list[2]

        user = util.searchUser(username)
        if user is None:
            return "No such user exists."

        if user.getUsername() is not None:
            if user.getPassword() == password:
                Command.setLogger(self, user)
                Command.setLogged(self, True)
                return username + " logged in."
            return "Wrong password."

        return "No such user exists."

    def isCommand(self, command):
        return command == "login"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
