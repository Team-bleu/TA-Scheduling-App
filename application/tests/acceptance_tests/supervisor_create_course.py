import unittest
from app import App
from UserUtility import UserUtility
from user import User


#2.

#As a supervisor I want to create a new course so that I can assign TA's and instructors.

class TestSupCreateCourse(unittest.TestCase):

    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "TA", None, None, None, None, None, None)

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

        self.assertEqual(self.app.command("createcourse CS352"), "CS352 has been created")

        self.assertEqual(self.app.command("assigncourse John CS352"), "John has been assigned to CS352")

        self.assertEqual(self.app.command("logout"), "logged out.")
        util = UserUtility()
        util.removeUser("John")

