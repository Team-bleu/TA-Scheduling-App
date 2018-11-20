from UserUtility import UserUtility
from Command import Command


class RoleCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"

        username = user_input_list[1]
        role = user_input_list[2]
        util = UserUtility()

        if not RoleCommand.checkRole(self, role):
            return role + " doesn't exist!"

        user = util.searchUser(username)

        if user is None:
            return username + " doesn't exist!"

        user.setRole(role)
        util.updateUser(user)

        return username + " has become a " + role

    def isCommand(self, command):
        return command == "role"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3

    def checkRole(self, role):
        if role == "Supervisor":
            return True
        if role == "Administrator":
            return True
        if role == "Instructor":
            return True
        if role == "TA":
            return True
        return False
