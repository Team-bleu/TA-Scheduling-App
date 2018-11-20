import unittest
from app import App
from UserUtility import UserUtility
from user import User


#8

#As an supervisor, I want to assign TAs to course so that later, the TAs can be assigned to a lab section

class TestSupAssignCourse(unittest.TestCase):

    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "TA", None, None, None, ["None"], ["None"], None)

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)
        
        self.assertEqual(self.app.command("assigncourse John CS351"), "John has been assigned to CS351")
        
        # not valid name
        self.assertEqual(self.app.command("assigncourse djofn CS351"), "djofn doesn't exist!")
        
        self.assertEqual(self.app.command("logout"), "logged out.")
