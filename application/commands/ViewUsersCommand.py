from Command import Command
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
        userFiles = userUtil.getAllUsers()

        accountsString = ""



        if (roleToCheck == "all"):
            accountsString = "All Users: \n\n"
            for i in range(0, userFiles.__len__()):
                # THE NEXT LINE OF CODE WILL BREAK DEPENDING ON THE OS BEING USED!!
                # MAC USERS MUST USE REPLACE: "application/data/users/" INSTEAD!!!
                # AND WINDOWS USERS MUST REPLACE: "application/data/users\\" INSTEAD!!
                username = userFiles[i] #.replace("application/data/users/", "").replace(".txt", "")
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





#NEW CODE
"""


    #   getAllUsers()
    #       returns a list of all of the users if there is at least one (users.txt should exist)
    #       return None if there are no users (users.txt would not exist)
    def getAllUsers(self):
        fileName = self.append("application/data/users/", "users") + ".txt"

        if (os.path.isfile(fileName)):  # check if file exists
            file = open(fileName, "r+")
            allUsers = file.readlines()
            file.close()
            for i in range(0, allUsers.__len__()):
                allUsers[i] = allUsers[i].replace("\n","")
            return allUsers
        else:
            # There are no courses
            return None



    #   addToMasterUserList() adds the user "userName" to users.txt (the file that keeps a list of all users)
    #       returns nothing
    def addToMasterUserList(self, userName):

        allUsers = self.getAllUsers()

        if (allUsers == None):  # there are no users yet  (users.txt doesn't exist yet)
            # create users.txt and add new user
            fileName = self.append("application/data/users/", "users") + ".txt"
            file = open(fileName, "+w")
            file.write(userName)
            file.close()
        else:
            # add usersName to allUsers list
            allUsers.append(userName)

            # write allUsers to users.txt
            fileName = self.append("application/data/users/", "users") + ".txt"
            file = open(fileName, "+w")
            for i in range(0, allUsers.__len__()):
                if (i == allUsers.__len__() - 1):
                    file.write(allUsers[i])
                else:
                    file.write(allUsers[i] + "\n")
            file.close()

        return



#   removeFromMasterUserList() removes the user "userName" from users.txt (the file that keeps a list of all courses)
    #       returns True if "userName" is removed from users.txt
    #       returns False if there are no users to remove
    def removeFromMasterUserList(self, userName):

        allUsers = self.getAllUsers()

        if (allUsers == None):  # there are no courses yet  (courses.txt doesn't exist yet)

            return False    # cannot remove anything, nothing exists!

        else:

            newSize = allUsers.__len__() - 1;

            # if new size is 0, delete users.txt because there are no courses left
            if (newSize == 0):
                fileName = self.append("application/data/courses/", "courses") + ".txt"
                os.remove(fileName)
                return True

            # create new list with new size
            newAllUsers = [None] * (newSize)
            index = 0;

            #put all users into newAllUsers list besides "userName" (the user to remove)
            for i in range(0,allUsers.__len__()):
                if (userName != allUsers[i]):
                    newAllUsers[index] = allUsers[i]
                    index = index + 1

            # set allCourse to the new "newAllUsers" list
            allUsers = newAllUsers

            #write allUsers to users.txt
            fileName = self.append("application/data/users/", "users") + ".txt"
            file = open(fileName, "+w")
            for i in range(0, allUsers.__len__()):
                if (i == allUsers.__len__()-1):
                    file.write(allUsers[i])
                else:
                    file.write(allUsers[i] + "\n")
            file.close()

        return True



"""





#OLD CODE BELOW
"""
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

        platString = platform.system()


        if (roleToCheck == "all"):
            accountsString = "All Users: \n\n"
            for i in range(0, userFiles.__len__()):
                # THE NEXT LINE OF CODE WILL BREAK DEPENDING ON THE OS BEING USED!!
                # MAC USERS MUST USE REPLACE: "application/data/users/" INSTEAD!!!
                # AND WINDOWS USERS MUST REPLACE: "application/data/users\\" INSTEAD!!
                if (platString == "Darwin"):
                    username = userFiles[i].replace("application/data/users/", "").replace(".txt", "")
                else:
                    username = userFiles[i].replace("application/data/users\\", "").replace(".txt", "")
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

"""