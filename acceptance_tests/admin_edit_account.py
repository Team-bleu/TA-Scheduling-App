import unittest
from app import App


#14.

#As an administrator, I want to be able to edit all the accounts of my TAs.

class TestAdminEditAccount(unittest.TestCase):

    app = App()
    # Mary is an administrator
	def test_login(self):
        self.assertEqual(self.app.command("login Mary password"), "Mary logged in")
    def test_edit_account(self):
        # John is a TA
		self.assertEqual(self.app.command("edit John"), "John's information has been updated")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Mary logged out")