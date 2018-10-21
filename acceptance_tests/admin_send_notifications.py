import unittest
from app import App


# 13.
# As an Administrator, I want to send out notifications
# via email, so that I can update people with new information
class AdminNotify(unittest.TestCase):
    app = App()

    # First we have the Administrator, Indigo, login
    # with <username>: Indigo and <password>: admin
    def test_login(self):
        self.assertEqual(self.app.command("login Indigo admin"), "Indigo logged in")

    # Then we have the Admin, Indigo, send a
    # notification to John, a TA
    def test_notify(self):
        self.assertEqual(self.app.command("notify John Don't forget to grade the assignments"),
                         "email has been sent")

    # Then we have the Admin logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Indigo logged out")
