import unittest
from app import App



class acceptanceTest(unittest.TestCase):
    app = App()

    # 7(Sprint 1) a Supervisor, I want to have a user interface so that I can login and logout my account
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("login user pass"), "No such user exists.")

    # 7(Sprint 1) a Supervisor, I want to have a user interface so that I can login and logout my account
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 3(Sprint 1) As a Supervisor, I want to create accounts

