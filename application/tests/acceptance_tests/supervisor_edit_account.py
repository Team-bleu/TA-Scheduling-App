import unittest
from application.app import App


#6.

#As a Supervisor, I want to be able to edit all the accounts of my TAs.

class TestSupEditAccount(unittest.TestCase):

    app = App()
    # James is a supervisor
    def test_login(self):
        self.assertEqual(self.app.command("login James password"), "James logged in")
    def test_edit_account(self):
        self.assertEqual(self.app.command("edit John"), "information updated") # John is a TA
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "James logged out")