import unittest
from app import App


#18.

#As an Instructor, I want to view course assignments so that I can see if any assignments need to be changed

class TestInstructorViewAssignments(unittest.TestCase):

    app = App()
    # Peter is an instructor
    def test_login(self):
        self.assertEqual(self.app.command("login Peter password"), "Peter logged in")
    def test_view(self):
        self.assertEqual(self.app.command("viewassignment CS351"), "viewed assignments for CS351")
        #Sally and John are TAs
        self.assertEqual(self.app.command("viewassignment Sally"), "viewed assignments for Sally")
        self.assertEqual(self.app.command("viewassignment John"), "viewed assignments for John")
        #not valid name
        self.assertEqual(self.app.command("viewassignment djofn"), "djofn does not exist")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Peter logged out")