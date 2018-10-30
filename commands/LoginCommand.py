from Command import Command
from BSTutility import BSTUtility


class LoginCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        util = BSTUtility()
        username = user_input_list[1]
        password = user_input_list[2]

        user = util.searchUser(username)

        if user.getUsername() != "None":
            if user.getPassword() == password:
                self.setCurrent(user)
                return username + " logged in."
            return "Wrong password."

        return "No such user exists."

    def isCommand(self, command):
        return command == "login"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
