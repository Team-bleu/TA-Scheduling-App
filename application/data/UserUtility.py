from user import User
import os
from TA_Scheduling_App.models import Account


class UserUtility:

    _directory = "./application/data/users/"
    _concat = ".txt"

    def __init__(self):
        self.setUp()

    def setUp(self):
        self._user = None

    def set_directory(self, directory):
        self._directory = directory

    def set_concat(self, concat):
        self._concat = concat

    def appendDir(self, file):
        return self._directory + file

    def appendTxt(self, file):
        return file + self._concat

    def removeNewLine(self, contents):
        i = 0
        for content in contents:
            contents[i] = content.replace("\n", "")
            i += 1
        return contents

    # Will create new user with contents following a list in the format:
    # (firstname, lastname, username, password , role,
    # information(phone, email, and address), course, lab, assignment)
    def createUser(self, contents):
        user = User(contents[0], contents[1], contents[2], contents[3], contents[4],
                    contents[5], contents[6], contents[7], contents[8], contents[9],
                    contents[10], contents[11])
        return user

    # This function searches for the user,
    # using their username and returns a User object
    def searchUser(self, username):
        file = self.appendTxt(username)
        file = self.appendDir(file)

        # If this user doesn't exist, return None
        if not os.path.isfile(file):
            return None

        file = open(file, "r+")
        contents = file.readlines()
        file.close()    # close file

        contents = self.removeNewLine(contents)

        if (contents.__len__ != 0):
            courseString = contents[8]
            courseList = courseString.split(",")
            contents[8] = courseList
            labString = contents[9]
            labList = labString.split(",")
            contents[9] = labList

        return self.createUser(contents)

    # This function will add a user, username
    def updateUser(self, user):
        # Search for the user file using the username
        username = user.getUsername()
        newuser = self.searchUser(username)

        if newuser is None:
            self.addUser(user)

        else:
            # Then remove that user and replace it with an updated one
            file = user.getUsername() + ".txt"
            os.remove(self._directory + file)
            self.addUser(user)

    def addUser(self, user):
        file = open(self._directory + user.getUsername() + self._concat, "w+")
        contents = user.getContents()
        courseList = list(contents[8])
        labList = list(contents[9])

        courseListString = ""
        labListString = ""

        # for courses
        for i in range(0,courseList.__len__()): # loop through courses and make them one string
            if (i != courseList.__len__()-1):
                courseListString = courseListString + courseList[i] + ","
            else:
                courseListString = courseListString + courseList[i]

        contents[8] = courseListString  # set contents[8] to the new courseListString

        # for labs
        for i in range(0,labList.__len__()): # loop through labs and make them one string
            if (i != labList.__len__()-1):
                labListString = labListString + labList[i] + ","
            else:
                labListString = labListString + labList[i]

        contents[9] = labListString  # set contents[9] to the new labListString

        for content in contents:
            if isinstance(content, list):
                for item in content:
                    if item is None:
                        file.write("None\n")
                    else:
                        item = item + "\n"
                        file.write(item)
            elif content is None:
                file.write("None\n")
            else:
                content = content + "\n"
                file.write(content)
        file.close()    #close file

        self.updateDB(user)

    def removeUser(self, username):
        user = self.searchUser(username)

        if user is None:
            return

        file = self._directory + user.getUsername() + self._concat
        os.remove(file)

        if not Account.objects.filter(username=user.getUsername()):
            return
        account = Account.objects.get(username=user.getUsername())
        account.delete()

    def updateDB(self, user):
        if Account.objects.filter(username=user.getUsername()):
            account = Account.objects.filter(username=user.getUsername())
            account.update(firstname=user.getFirstName(), lastname=user.getLastName(),
                           username=user.getUsername(), password=user.getPassword(), role=user.getRole(),
                           phone=user.getPhone(), email=user.getEmail(), address=user.getAddress(),
                           course=user.getCourses(), lab=user.getLabs(), assignment=user.getAssignment(),
                           officehours=user.getOfficeHours())
        else:
            account = Account(firstname=user.getFirstName(), lastname=user.getLastName(),
                              username=user.getUsername(), password=user.getPassword(), role=user.getRole(),
                              phone=user.getPhone(), email=user.getEmail(), address=user.getAddress(),
                              course=user.getCourses(), lab=user.getLabs(), assignment=user.getAssignment(),
                              officehours=user.getOfficeHours())
            account.save()





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
            # There are no users
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



    #   removeFromMasterUserList() removes the user "userName" from users.txt (the file that keeps a list of all users)
    #       returns True if "userName" is removed from users.txt
    #       returns False if there are no users to remove
    def removeFromMasterUserList(self, userName):

        allUsers = self.getAllUsers()

        if (allUsers == None):  # there are no users yet  (users.txt doesn't exist yet)

            return False    # cannot remove anything, nothing exists!

        else:

            newSize = allUsers.__len__() - 1;

            # if new size is 0, delete users.txt because there are no users left
            if (newSize == 0):
                fileName = self.append("application/data/users/", "users") + ".txt"
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

            # set allUsers to the new "newAllUsers" list
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



    #   append() is used to append two strings together
    #       In particular, this function appends a directory with a file
    #       returns the two strings "directory" and "file" as one combined string
    def append(self, directory, file):
        return directory + file