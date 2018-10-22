import unittest
from app import App


#6.

#As a Supervisor, I want to be able to edit all the accounts of my TAs.

class TestSupEditAccount(unittest.TestCase):

    app = App()

    # James is a supervisor
    def test_login(self):
        self.assertEqual(self.app.command("login James password"), "James logged in")
    def test_edit_account(self):
        # John is a TA
		self.assertEqual(self.app.command("edit John"), "John's information has been updated")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "James logged out")