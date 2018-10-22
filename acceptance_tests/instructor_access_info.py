

import unittest
from app import App


# 19 As an instructor, I want to read public contact information of TA's assigned and my own information
#All public contact information from the TA's and other instructors should be print on the screen
class TestInsAccessInfo(unittest.TestCase):
    app = App()
    infor = {"username": "John", "role": "TA", "phone": "999-930-9999", "email":"john@uwm.edu", "course" : "cs250",
             "lab": "section802"}
    # First we have the instructor login
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")
    # nest we have the Instructor call view on John
    # Then we delete an account


    def test_view(self):
        self.assertEqual(self.app.command("view John"), self.infor)


    # Then we have Instructor logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")

