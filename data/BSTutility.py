from user import User
import os


class BSTUtility:

    _user = None
    _root = None
    _current = None
    _parent = None
    _leftChild = None
    _rightChild = None

    def __init__(self):
        self.setUp()

    # Sets up the Binary Search Tree Utility, will retrieve
    # a root, current, left child, and right child
    def setUp(self):
        self._root = self.setUpRoot()
        self._current = self._root
        self._leftChild = self.getLeftChild()
        self._rightChild = self.getRightChild()

    # This function is used to append two strings together
    # In particular, this function appends a directory with a file
    def append(self, directory, file):
        return directory + file

    # This function removes the newline character
    def removeNewLine(self, contents):
        i = 0
        for content in contents:
            contents[i] = content.replace("\n", "")
            i += 1
        return contents

    def setUpRoot(self):
        # Opens the root text file which
        # stores the name of the root file
        root = open("data/root.txt", "r+")
        rootname = root.readlines()

        # Opens the root file
        rootname = self.append("data/users/", rootname[0])
        file = open(rootname, "r+")
        contents = file.readlines()
        self.removeNewLine(contents)

        return self.createUser(contents)

    # Will create new user with contents following a list in the format:
    # (firstname, lastname, username, password ,
    # role, information(phone, email, and address), course, lab,
    # assignment, parent, leftChild, rightChild)
    def createUser(self, contents):
        return User(contents[0], contents[1], contents[2], contents[3], contents[4],
                    [contents[5], contents[6], contents[7]], contents[8], contents[9],
                    contents[10], contents[11], contents[12], contents[13])

    def createEmptyUser(self):
        return User()

    # This function grabs the left child based off of the _current
    def getLeftChild(self):
        # If no left child exists return immediately
        if self._current.getLeftChild() == "None":
            return User()
        filename = self._current.getLeftChild()
        filename = self.append("data/users/", filename)
        file = open(filename, "r+")
        contents = file.readlines()
        self.removeNewLine(contents)
        return self.createUser(contents)

    # This function grabs the left child based off of the _current
    def getRightChild(self):
        # If no right child exists return immediately
        if self._current.getRightChild() == "None":
            return User()
        filename = self._current.getRightChild()
        filename = self.append("data/users/", filename)
        file = open(filename, "r+")
        contents = file.readlines()
        self.removeNewLine(contents)
        return self.createUser(contents)

    # This function traverses the left subtree
    def traverseLeft(self):
        self._parent = self._current
        self._current = self._leftChild
        self._leftChild = self.getLeftChild()
        self._rightChild = self.getRightChild()

    # This function traverses the right subtree
    def traverseRight(self):
        self._parent = self._current
        self._current = self._rightChild
        self._leftChild = self.getLeftChild()
        self._rightChild = self.getRightChild()

    # This function searches for the user,
    # using their username and returns a User object
    # This is a recursive method
    def searchUser(self, username):
        if self._current.getUsername() == "None":
            return self.createEmptyUser()
        if username == self._current.getUsername():
            return self._current
        elif username < self._current.getUsername():
            self.traverseLeft()
            return self.searchUser(username)
        else:
            self.traverseRight()
            return self.searchUser(username)

    # This function should add a user, username
    # Must traverse the tree to find the correct spot
    # to be in, will update parent, left child, and
    # right child of self and surrounding neighbors
    def updateUser(self, user):
        # Must call setUp to reset current, parent, left child, and right child
        self.setUp()

        # Search for the user file using the username
        username = user.getUsername()
        newuser = self.searchUser(username)

        # Before we add or edit a user, we must
        # change the user-to-be-added's parent to match
        user.setParent(self._parent)

        # If user doesn't exist, create a new user
        if newuser.getUsername() == "None":
            self.addUser(user)

        # If user exists update current existing user
        else:
            # Then remove that user and replace it with an updated one
            file = user.getUsername() + ".txt"
            os.remove("data/users/" + file)
            self.addUser(user)

    def addUser(self, user):
        # Update the new location to get a parent pointer
        self.searchUser(user.getUsername())

        # Creates a new file to store the new user
        # The nested for loops take into account the
        # information list and None existing parent and child
        file = open("data/users/" + user.getUsername() + ".txt", "w+")
        contents = user.getContents()
        for content in contents:
            if isinstance(content, list):
                for item in content:
                    item = item + "\n"
                    file.write(item)
            elif isinstance(content, User):
                if content.getUsername() == "None":
                    file.write("None\n")
                else:
                    content = content.getUsername() + ".txt\n"
                    file.write(content)
            else:
                content = content + "\n"
                file.write(content)

        # Now we must make sure to have the parent's child's
        # correct after the addition of the new user
        file = user.getUsername() + ".txt"
        if (file != self._parent.getLeftChild()) and \
                (file != self._parent.getRightChild()):
            if self._parent.getUsername() + ".txt" > file:
                self._parent.setLeftChild(file)
            else:
                self._parent.setRightChild(file)
            self.updateUser(self._parent)

    # This function should remove a user, username
    # Must traverse the tree to find the correct user
    # to remove, will update parent, left child, and
    # right child of self and surrounding neighbors
    def removeUser(self, username):
        # Reset positions and update the location of user
        self.setUp()
        user = self.searchUser(username)
        file = username + ".txt"

        # If that user doesn't exist in the tree
        # ignore and return nothing
        if user.getUsername() == "None":
            return

        # If the user to be removed is the parent's left child,
        # replace the parent's left child with the current's left child
        if file == self._parent.getLeftChild():
            self._parent.setLeftChild(user.getLeftChild())
            self.updateUser(self._parent)

            # Then search the right subtree of the parent to store
            # the right subtree of current
            right = self.getRightChild()
            if right.getUsername() != "None":
                self.updateUser(right)

        # Otherwise, the user to be removed is the parent's right child
        # and replace the parent's right child with the current's right child
        else:
            self._parent.setRightChild(user.getRightChild())
            self.updateUser(self._parent)

            # Then search the left subtree of the parent to store the
            # left subtree of current
            left = self.getLeftChild()
            if left.getUsername() != "None":
                self.updateUser(left)

        # Finally, remove the user
        file = "data/users/" + user.getUsername() + ".txt"
        os.remove(file)


# # This tests the utility
# obj = BSTUtility()
# obj.setUpRoot()
# print("root is " + obj._root.getUsername())
# print("left child is " + obj._leftChild.getUsername())
# print("right child is " + obj._rightChild.getUsername())
# print("done\n")
#
# # This is findme.txt and should print an object pointing to it and name in file
# user = obj.searchUser("findme")
# print("searched for user: findme and obtained object:")
# print(user)
# print("first name: " + user.getFirstName())
# print("last name: " + user.getLastName())
# print("found username: " + user.getUsername())
#
# # This is used to see if we can find a non-existing user
# user = obj.searchUser("dontexist")
# print("\nthe username dontexist, doesn't exist; and the object made form it is:")
# print(user)
# print("first name: " + user.getFirstName())
# print("last name: " + user.getLastName())
# print("found username: " + user.getUsername())
#
# # # This is to test the functionality of updateUser
# # obj.updateUser(User("New", "Dude", "findme", "pass", "role", ["newphone", "newemail", "address"], "course", "lab",
# #                     "None", "None", "None", "None"))
# # # This is to test the functionality of addUser
# # obj.updateUser(User("a", "b", "ab", "pass", "role", ["phone", "email", "address"], "course", "lab",
# #                     "None", "None", "None", "None"))
# # obj.updateUser(User("zz", "z", "zz", "pass", "role", ["phone", "email", "address"], "course", "lab",
# #                     "None", "None", "None", "None"))
#
# # To test correctly, delete guy.txt before running this code
# obj.updateUser(User("THe", "Guy", "guy", "pass", "role", ["phone", "email", "address"], "course", "lab",
#                     "None", "None", "None", "None"))
# obj.removeUser("guy")
