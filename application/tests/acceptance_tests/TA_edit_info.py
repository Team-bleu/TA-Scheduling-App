import unittest
from application.app import App


# 24 

# As a TA I want to edit my own information so that the administrator and supervisor have access to it

class TestTAInfo(unittest.TestCase):

    app = App()

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        
        self.assertEqual(self.app.command("edit super"), "information updated")

        # not valid name
        self.assertEqual(self.app.command("viewassignment djofn"), None) # djofn does not exist
        
        self.assertEqual(self.app.command("logout"), "logged out.")
