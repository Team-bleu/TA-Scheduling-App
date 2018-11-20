import unittest
from app import App
from UserUtility import UserUtility
from user import User


#As an Administrator, I want to be able to delete accounts.
class TestAdmDeleteAccount(unittest.TestCase):
    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, None, None, None, None, None, None, None)

    # First we have the admin login
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

    # Then we delete an account
        self.assertEqual(self.app.command("remove John"), "John has been removed.")


    # Then we have admin logout
        self.assertEqual(self.app.command("logout"), "logged out.")
        # For testing purposes, we will delete Tom
        util = UserUtility()
        util.removeUser("John")

#3,7,11,15, 19, 23