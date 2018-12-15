from Command import Command
import glob
from UserUtility import UserUtility


class ViewUsersCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        roleToCheck = user_input_list[1]

        if (roleToCheck != "Supervisor" and
                roleToCheck != "Administrator" and
                roleToCheck != "Instructor" and
                roleToCheck != "TA" and
                roleToCheck != "all"):
            return "Not a valid role"

        userUtil = UserUtility()
        path = "application/data/users/*.txt"
        userFiles = glob.glob(path)

        accountsString = ""


        if (roleToCheck == "all"):
            accountsString = "All Users: \n\n"
            for i in range(0, userFiles.__len__()):
                # THE NEXT LINE OF CODE WILL BREAK DEPENDING ON THE OS BEING USED!!
                # MAC USERS MUST USE REPLACE: "application/data/users/" INSTEAD!!!
                # AND WINDOWS USERS MUST REPLACE: "application/data/users\\" INSTEAD!!
                username = userFiles[i].replace("application/data/users/", "").replace(".txt", "")
                user = userUtil.searchUser(username)
                userRole = user.getRole();
                userFirstName = user.getFirstName()
                userLastName = user.getLastName()
                userEmail = user.getEmail();
                accountsString = accountsString + "User: " + username + "\n" \
                                                   "First name: " + userFirstName + "\n" \
                                                   "Last name: " + userLastName + "\n" \
                                                   "Role: " + userRole + "\n" \
                                                   "Email: " + userEmail + "\n\n"
        else:
            accountsString = roleToCheck + "s: \n\n"
            for i in range(0, userFiles.__len__()):
                username = userFiles[i].replace("application/data/users/","").replace(".txt","")
                user = userUtil.searchUser(username)
                userRole = user.getRole();
                if (userRole == roleToCheck):
                    userFirstName = user.getFirstName()
                    userLastName = user.getLastName()
                    userEmail = user.getEmail();
                    accountsString = accountsString + "User: "+ username + "\n" \
                                                      "First name: "+ userFirstName + "\n" \
                                                      "Last name: "+ userLastName + "\n" \
                                                      "Role: " + userRole + "\n" \
                                                      "Email: "+ userEmail + "\n\n"

        return accountsString

    def isCommand(self, command):
        return command == "viewusers"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
