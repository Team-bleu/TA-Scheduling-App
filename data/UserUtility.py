from user import User
import os


class UserUtility:

    _directory = "../data/users/"
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
                    contents[10])
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

        contents = self.removeNewLine(contents)
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

    def removeUser(self, username):
        user = self.searchUser(username)

        if user is None:
            return

        file = self._directory + user.getUsername() + self._concat
        os.remove(file)
