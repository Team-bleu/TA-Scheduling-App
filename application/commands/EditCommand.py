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

        length = len(user_input_list)
        index = 2
        while index < length:
            if user_input_list[index] == "phone":
                index += 1
                user.setPhone(user_input_list[index])
            elif user_input_list[index] == "email":
                index += 1
                user.setEmail(user_input_list[index])
            elif user_input_list[index] == "address":
                index += 1
                user.setAddress(EditCommand.getAddress(self, user_input_list, index, length))
            elif user_input_list[index] == "firstname":
                index += 1
                user.setFirstName(user_input_list[index])
            elif user_input_list[index] == "lastname":
                index += 1
                user.setLastName(user_input_list[index])
            else:
                index += 1

        util.updateUser(user)

        return "information updated"

    def isCommand(self, command):
        return command == "edit"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2

    def getAddress(self, user_input_list, index, length):
        string = ""
        while index < length:
            if user_input_list[index] == "phone" or user_input_list[index] == "email" or \
                    user_input_list[index] == "address" or user_input_list[index] == "firstname" or \
                    user_input_list[index] == "lastname":
                return string
            string = string + user_input_list[index] + " "
            index += 1
        return string
