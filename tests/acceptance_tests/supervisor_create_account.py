import unittest
from app import App


#3As a Supervisor, I want to create accounts and edit those accounts so that I can add TA's and edit their contact info
class TestSupCreateAccount(unittest.TestCase):
    app = App()

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then we add a new user
    def test_add(self):
        self.assertEqual(self.app.command("add Tom admin"), "User Tom added")


    # Then we have them logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")

