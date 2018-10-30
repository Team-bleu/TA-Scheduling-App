from Command import Command
from BSTutility import BSTUtility
from user import User


class AddCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        util = BSTUtility()
        username = user_input_list[1]
        password = user_input_list[2]

        user = util.searchUser(username)

        if user.getUsername() != "None":
            return "User already exists."

        # user is empty user: User("first", "last", username, password, "role",
        # ["phone", "email", "address"], "course", "lab",
        # "assignment", "None", "None", "None")
        user = User()

        user.setAccount(username, password)

        util.updateUser(user)

        return username + " has been added"

    def isCommand(self, command):
        return command == "add"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
