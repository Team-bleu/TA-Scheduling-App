import unittest
from app import App


#15 As an administrator I want to create courses so that later I can assign instructors and TAs to their courses.
class TestAdmCreateAccount(unittest.TestCase):
    app = App()

    # First we have the admin login
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then we add a new user
    def test_add(self):
        self.assertEqual(self.app.command("add Tom admin"), "User Tom added")


    # Then we have admin logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")

