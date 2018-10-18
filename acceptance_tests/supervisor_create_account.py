import unittest
from app import App


# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester
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

