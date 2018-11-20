import unittest
from application.app import App


# 16

# As an Administrator, I want to access all the data in the system

class TestAdminInfo(unittest.TestCase):

    app = App()
    # Peter is an instructor
    
    def test_login(self):
        self.assertEqual(self.app.command("login Peter password"), "Peter logged in")
        
    def test_show(self):
        self.assertEqual(self.app.command("show John"), "John's information: ")
        
        # not valid name
        
        self.assertEqual(self.app.command("show djofn"), "djofn does not exist")
        
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Peter has logged out")