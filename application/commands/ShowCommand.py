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

        string = ""

        if user_rank <= 2:
            string = "First Name: " + user.getFirstName() + "\nLast Name: " + user.getLastName() \
                     + "\nemail: " + user.getEmail()
        else:
            if user.getFirstName() is None:
                string = "First Name: None"
            else:
                string = string + "First Name: " + user.getFirstName()
            if user.getLastName() is None:
                string = string + "\nLast Name: None"
            else:
                string = string + "\nLast Name: " + user.getLastName()
            if user.getEmail() is None:
                string = string + "\nemail: None"
            else:
                string = string + "\nemail: " + user.getEmail()
            if user.getPassword() is None:
                string = string + "\nphone: None"
            else:
                string = string + "\nphone: " + user.getPhone()
            if user.getAddress() is None:
                string = string + "\naddress: None"
            else:
                string = string + "\naddress: " + user.getAddress()

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
