import unittest
from app import App
from UserUtility import UserUtility
from user import User

# 4

# As a supervisor, I want to delete an account so that the account isn't accessible anymore (for when employees leave)

class TestSupDelAccount(unittest.TestCase):

    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "TA", None, None, None, None, None, None)

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)
        
        # John is a TA
        self.assertEqual(self.app.command("remove John"), "John has been removed.")
        # not valid name
        self.assertEqual(self.app.command("remove djofn"), "djofn doesn't exist!")
        
        self.assertEqual(self.app.command("logout"), "logged out.")
