import unittest
from app import App
from UserUtility import UserUtility


#15 As an administrator I want to create courses so that later I can assign instructors and TAs to their courses.
class TestAdmCreateAccount(unittest.TestCase):
    app = App()

    # First we have the admin login
    def test_admin_create_acount(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

    # Then we add a new user
        self.assertEqual(self.app.command("add Tom admin"), "Tom has been added")

    # Then we have admin logout
        self.assertEqual(self.app.command("logout"), "logged out.")

    # For testing purposes, we will delete Tom
        util = UserUtility()
        util.removeUser("Tom")

