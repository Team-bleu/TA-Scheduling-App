import unittest
from acceptance_test_UI import AcceptanceUI


class SupAssignTALab(AcceptanceUI, unittest.TestCase):

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login " + self.users[3]["username"] + " " + self.users[3]["password"]),
                         self.users[3]["username"] + " logged in")

    def test_logout(self):
        self.assertEqual(self.app.command("logout"), self.users[3]["username"] + " logged out")
