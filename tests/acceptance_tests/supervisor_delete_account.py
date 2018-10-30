import unittest
from app import App


# 4

# As a supervisor, I want to delete an account so that the account isn't accessible anymore (for when employees leave)

class TestSupDelAccount(unittest.TestCase):

    app = App()
    # Peter is an supervisor
    
    def test_login(self):
        self.assertEqual(self.app.command("login Peter password"), "Peter logged in")
        
    def test_remove(self):
        # John is a TA
        self.assertEqual(self.app.command("remove John"), "John has been added to course")
        # not valid name
        self.assertEqual(self.app.command("remove djofn"), "djofn does not exist")
        
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Peter logged out") 