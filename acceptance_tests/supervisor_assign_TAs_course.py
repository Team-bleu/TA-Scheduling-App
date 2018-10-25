import unittest
from app import App


#8

#As an supervisor, I want to assign TAs to course so that later, the TAs can be assigned to a lab section

class TestSupAssignCourse(unittest.TestCase):

    app = App()
    # Peter is an instructor
    def test_login(self):
        self.assertEqual(self.app.command("login Peter password"), "Peter logged in")
        
    def test_assigncourse(self):
        self.assertEqual(self.app.command("asigncourse John CS351"), "John has been added to CS351")
        
        #not valid name
        self.assertEqual(self.app.command("assigncourse djofn"), "djofn does not exist")
        
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Peter logged out")