from Command import Command
from BSTutility import BSTUtility
from user import User
from CommandsList import CommandsList



class AddCommand(Command):

    def action(self, user_input_list):
        if not CommandsList.getCredentialss() >= 3:
            return "Error. Current User does not have permission to create a user."

        util = BSTUtility()
        username = user_input_list[1]
        password = user_input_list[2]

        user = util.searchUser(username)

        if user is not None and user.getUsername() is not None:
            return "User already exists."

        user = User("first", "last", username, password, "role",
                    "phone", "email", "address", "course", "lab", "assignment", "None", "None", "None")
        # user = User()

        user.setAccount(username, password)

        util.updateUser(user)

        return username + " has been added"

    def isCommand(self, command):
        return command == "add"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
