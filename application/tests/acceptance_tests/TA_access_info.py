import unittest
from application.app import App


# 23 As an TA, I want to read public contact information of the users
# All public contact information from the TA's and other instructors should be print on the screen

class TestTAAccessInfo(unittest.TestCase):
    app = App()
    # First we have the instructor login
    infor = {"username": "John", "role": "TA", "phone": "999-930-9999", "email": "john@uwm.edu", "course": "cs250",
             "lab": "section802"}

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

    # nest we have the Instructor call view on John
    # Then we delete an account

        self.assertEqual(self.app.command("view John"), self.infor)

    # Then we have Instructor logout
        self.assertEqual(self.app.command("logout"), "logged out.")

