import unittest
from app import App


#7 a Supervisor, I want to have a user interface so that I can login and logout my account
class TestSupLoginLogout(unittest.TestCase):
    app = App()

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then we have them logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")

