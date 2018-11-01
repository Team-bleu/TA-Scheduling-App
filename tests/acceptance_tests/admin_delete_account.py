import unittest
from app import App


#As an Administrator, I want to be able to delete accounts.
class TestAdmDeleteAccount(unittest.TestCase):
    app = App()

    # First we have the admin login
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then we delete an account
    def test_remove(self):
        self.assertEqual(self.app.command("remove John"), "John has been remoed")


    # Then we have admin logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")

#3,7,11,15, 19, 23