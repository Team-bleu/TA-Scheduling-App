import unittest
from app import App


# 24 

# As a TA I want to edit my own information so that the administrator and supervisor have access to it

class TestTAInfo(unittest.TestCase):

    app = App()
    # Peter is an instructor
    
    def test_login(self):
        self.assertEqual(self.app.command("login Peter password"), "Peter logged in")
        
    def test_edit(self):
        self.assertEqual(self.app.command("edit CS351"), "information updated")

        # not valid name
        self.assertEqual(self.app.command("viewassignment djofn"), "djofn does not exist")
        
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Peter has logged out")