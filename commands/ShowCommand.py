from UserUtility import UserUtility
from Command import Command


class ShowCommand(Command):

    def action(self, user_input_list):
        if not Command.isLogged(self):
            return "No user is logged in."

        util = UserUtility()
        username = user_input_list[1]
        user = util.searchUser(username)
        if user is None:
            return username + " doesn't exist!"

        user_rank = Command.getCredentialss(self)
        role = user.getRole()
        search_rank = ShowCommand.checkRank(self, role)

        if user_rank < search_rank:
            return "You do not have permission to view " + username

        if user_rank <= 2:
            string = "First Name: " + user.getFirstName() + "\nLast Name: " + user.getLastName() \
                     + "\nemail: " + user.getEmail()
        else:
            string = "First Name: " + user.getFirstName() + "\nLast Name: " + user.getLastName() \
                     + "\nemail: " + user.getEmail() + "\nphone: " + user.getPhone() \
                     + "\naddress: " + user.getAddress()

        return string

    def isCommand(self, command):
        return command == "show"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2

    def checkRank(self, role):
        rank = 0

        if role == "Supervisor":
            rank = 4
        if role == "Administrator":
            rank = 3
        if role == "Instructor":
            rank = 2
        if role == "TA":
            rank = 1
        return rank
