import unittest
from app import App


#10.

#As a Supervisor, I want to send out notification via UWM Email

class TestSupNotify(unittest.TestCase):

    app = App()

	def test_login(self):
        self.assertEqual(self.app.command("login James password"), "James logged in")
    def test_notify(self):
		self.assertEqual(self.app.command("notify John Classes are cancelled today!"), "Email has been sent.")
    def test_logout(self):