import unittest
from app import App


#18.

#As an Instructor, I want to view course assignments so that I can see if any assignments need to be changed

class TestInstructorViewAssignments(unittest.TestCase):

    app = App()

	def test_login(self):
        self.assertEqual(self.app.command("login James password"), "James logged in")
    def test_notify(self):
		self.assertEqual(self.app.command("view CS351"), "viewed CS351 assignments")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "James logged out")