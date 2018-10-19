import unittest
from app import App


#22.

#As a TA, I want to view all the TA assignments.

class TestTAViewAssignments(unittest.TestCase):

    app = App()

	def test_login(self):
        self.assertEqual(self.app.command("login James password"), "James logged in")
    def test_notify(self):
		self.assertEqual(self.app.command("view CS351"), "viewed CS351 assignments")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "James logged out")