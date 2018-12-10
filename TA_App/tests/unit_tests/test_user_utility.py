from django.test import TestCase
from UserUtility import UserUtility
from user import User


class UserUtilityTest(TestCase):

    def test_appendDir(self):
        util = UserUtility()
        self.assertEqual(util.appendDir("test"), "./application/data/users/test")

    def test_appendTxt(self):
        util = UserUtility()
        self.assertEqual(util.appendTxt("test"), "test.txt")

    def test_removeNewLine(self):
        util = UserUtility()
        self.assertEqual(util.removeNewLine(["test\n"]), ["test"])
        self.assertEqual(util.removeNewLine(["test\n\n"]), ["test"])
        self.assertEqual(util.removeNewLine(["test"]), ["test"])

    def test_createUser(self):
        util = UserUtility()
        self.assertEqual(util.createUser(["first", "last", "username", "pass", "role",
                                          "phone", "email", "address", "course", "lab",
                                          "assignment", "officehours"]).getContents(),
                         User("first", "last", "username", "pass", "role",
                              "phone", "email", "address", "course", "lab",
                              "assignment", "officehours").getContents())

    def test_search_user(self):
        util = UserUtility()
        searchuser = User("first", "last", "searchuser", "password", "role",
                          "phone", "email", "address", ["None"], ["None"],  "assignment", "officehours")
        util.updateUser(searchuser)
        self.assertIsNone(util.searchUser("NotExist"))

        # We must reset the utility before looking for the new user
        util.setUp()
        self.assertIsInstance(util.searchUser("searchuser"), User)
        self.assertEqual(util.searchUser("searchuser").getContents(), searchuser.getContents())
        # Now we must reset the utility and remove the dummy user
        # But the line below doesn't work. Manually delete searchuser.txt
        # and update the neighbors.
        self.assertIsNone(util.removeUser("searchuser"))

    def test_update_user(self):
        util = UserUtility()
        searchuser = User("first", "last", "searchuser", "password", "role",
                          "phone", "email", "address", ["None"], ["None"], "assignment", "officehours")
        util.updateUser(searchuser)

        # If the user "searchuser" has been added correctly, we can verify its contents
        self.assertEqual(util.searchUser("searchuser").getContents(), searchuser.getContents())
        self.assertIsNone(util.removeUser("searchuser"))

    def test_add_user(self):
        util = UserUtility()
        searchuser = User("first", "last", "searchuser", "password", "role",
                          "phone", "email", "address", ["None"], ["None"], "assignment", "officehours")
        util.addUser(searchuser)
        # If the user "searchuser" has been added correctly, we can verify its contents
        # same reason as update user test
        self.assertEqual(util.searchUser("searchuser").getContents(), searchuser.getContents())
        self.assertIsNone(util.removeUser("searchuser"))

    def test_remove_user(self):
        util = UserUtility()
        self.assertIsNone(util.removeUser("NotExist"))
