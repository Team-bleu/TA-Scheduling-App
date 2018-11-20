import unittest
from app import App
from UserUtility import UserUtility


# 3As a Supervisor, I want to create accounts and edit those accounts so that I can add TA's and edit their contact info
class TestSupCreateAccount2(unittest.TestCase):
    app = App()

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

    # Then we add a new user
        self.assertEqual(self.app.command("add Tom admin"), "Tom has been added")

    # Then we have them logout
        self.assertEqual(self.app.command("logout"), "logged out.")
        util = UserUtility()
        util.removeUser("Tom")
