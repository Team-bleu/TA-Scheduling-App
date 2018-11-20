import unittest
from app import App
from UserUtility import UserUtility
from user import User


#10.

#As a Supervisor, I want to send out notification via UWM Email

class TestSupNotify(unittest.TestCase):

    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "TA", None, None, None, None, None, None)

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

        self.assertEqual(self.app.command("notify John Classes are cancelled today!"), None)

        self.assertEqual(self.app.command("logout"), "logged out.")
        util = UserUtility()
        util.removeUser("John")
