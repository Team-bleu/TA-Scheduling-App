import unittest
from app import App
from UserUtility import UserUtility
from user import User


#14.

#As an administrator, I want to be able to edit all the accounts of my TAs.

class TestAdminEditAccount(unittest.TestCase):

    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, None, None, None, None, None, None, None)

    # Super is an administrator
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

        # John is a TA
        self.assertEqual(self.app.command("edit John"), "information updated")

        self.assertEqual(self.app.command("logout"), "logged out.")

