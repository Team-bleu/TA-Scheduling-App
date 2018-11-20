import unittest
from app import App
from UserUtility import UserUtility
from user import User


# 13.
# As an Administrator, I want to send out notifications
# via email, so that I can update people with new information
class TestAdminNotify(unittest.TestCase):
    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, None, None, None, None, None, None, None)

    # First we have the Administrator, login
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

    # For testing purposes we'll add a John
        self.util.updateUser(self.user)

    # Then we have the Admin, send a
    # notification to John, a TA
        self.assertEqual(self.app.command("notify John Don't forget to grade the assignments"), None)

    # Then we have the Admin logout
        self.assertEqual(self.app.command("logout"), "logged out.")


